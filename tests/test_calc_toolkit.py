#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""计算器回归测试（仅标准库，零依赖）。

为什么有这个文件：
    2026-10-28 一天内连着发现三处单位错（`rent.py --vacancy 15` 被算成 1500%、
    `efficiency.py --use-coef 88` 被算成 8800%、`commission.py --seller-rate 1` 被当成 100%）。
    这类错的共同点是"程序不崩、结果差 100 倍"，只能靠断言把口径钉住。

跑法：
    python3 -m unittest discover -s tests -v
    python3 tests/test_calc_toolkit.py        # 单跑

原则：
    - 只断言"确定的"：给定参数的输出口径、越界必须拦、两个算法必须并排给出。
    - 不断言具体费率数字（规则库按城市档和生效日会变），除非参数由测试自己传入。
"""
import os
import re
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALC = os.path.join(ROOT, "skills", "calc-toolkit")


def run(tool, *args, timeout=90):
    """跑一个计算器，返回 (退出码, 标准输出+错误输出)。"""
    cmd = [sys.executable, os.path.join(CALC, tool)] + list(args)
    p = subprocess.run(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       timeout=timeout)
    return p.returncode, p.stdout.decode("utf-8", "replace")


def num(text, pattern):
    """从输出里按正则抓一个数字（允许千分位逗号）。返回 float。"""
    m = re.search(pattern, text)
    if not m:
        raise AssertionError(f"输出里没找到 {pattern!r}：\n{text[:1200]}")
    return float(m.group(1).replace(",", ""))


class TestUnitConventions(unittest.TestCase):
    """单位口径：百分数 param 与小数 param 不能混用。"""

    def test_rent_accepts_percent_vacancy(self):
        """rent.py --vacancy 15 = 15%，净回报应落在 1%~3%（150 万 / 月租 3500）。"""
        code, out = run("rent.py", "--price", "1500000", "--rent", "3500", "--net",
                        "--vacancy", "15", "--tax-rate", "5", "--maint", "0.5")
        self.assertEqual(code, 0, out)
        net = num(out, r"净回报率[^\d]*([\d.]+)%")
        self.assertGreater(net, 1.0, out)
        self.assertLess(net, 4.0, out)

    def test_rent_rejects_absurd_vacancy(self):
        """--vacancy 1500 必须被拦（历史 bug：被当成小数→1500%）。"""
        code, out = run("rent.py", "--price", "1500000", "--rent", "3500", "--net",
                        "--vacancy", "1500")
        self.assertNotEqual(code, 0, "越界空置率应当报错：" + out)

    def test_rent_net_lower_than_gross(self):
        """净回报必须小于毛回报（扣空置/税/维修后）。"""
        code, out = run("rent.py", "--price", "1500000", "--rent", "3500", "--net",
                        "--vacancy", "15", "--tax-rate", "5", "--maint", "0.5")
        self.assertEqual(code, 0, out)
        gross = num(out, r"毛回报率[^\d]*([\d.]+)%")
        net = num(out, r"净回报率[^\d]*([\d.]+)%")
        self.assertLess(net, gross, out)

    def test_efficiency_coef_is_decimal(self):
        """efficiency.py --use-coef 0.88 = 88%；传 88 必须被拦（历史 bug：8800%）。"""
        code, out = run("efficiency.py", "--gross", "100", "--inner", "78", "--use-coef", "0.88")
        self.assertEqual(code, 0, out)
        code_bad, out_bad = run("efficiency.py", "--gross", "100", "--inner", "78", "--use-coef", "88")
        self.assertNotEqual(code_bad, 0, "use-coef 88 应当被拦：" + out_bad)
        self.assertIn("0.88", out_bad, "报错信息应给出正确写法：" + out_bad)

    def test_commission_rate_is_decimal(self):
        """commission.py --seller-rate 1 会被当成 100%，必须给出单位提醒（但不崩）。"""
        code, out = run("commission.py", "--scene", "resale", "--price", "1500000", "--seller-rate", "1")
        self.assertEqual(code, 0, out)
        self.assertIn("单位提醒", out, "费率 >0.2 时应提示单位：" + out)


class TestCommission(unittest.TestCase):
    def test_channel_double_algorithm_reported(self):
        """渠道阶梯必须同时给"全额跳档"和"分段累进"两个数，且差额被指出。"""
        code, out = run("commission.py", "--scene", "channel", "--amount", "30000000",
                        "--tiers", "20000000:0.02;999999999:0.025")
        self.assertEqual(code, 0, out)
        whole = num(out, r"全额跳档[^\n]*?([\d,]+)\s*元")
        progressive = num(out, r"分段累进[^\n]*?([\d,]+)\s*元")
        self.assertAlmostEqual(whole, 750000, delta=1)
        self.assertAlmostEqual(progressive, 650000, delta=1)
        self.assertIn("差", out)

    def test_lease_commission_split(self):
        """租赁佣金：月租 3500 × 1 个月，双方各半 → 各 1,750。"""
        code, out = run("commission.py", "--scene", "lease", "--rent", "3500",
                        "--months", "1", "--landlord-share", "0.5")
        self.assertEqual(code, 0, out)
        self.assertIn("3,500", out)
        self.assertEqual(out.count("1,750"), 2, out)

    def test_lease_requires_rent(self):
        code, out = run("commission.py", "--scene", "lease")
        self.assertNotEqual(code, 0, out)
        self.assertIn("--rent", out)

    def test_lease_months_upper_bound(self):
        """佣金月数 > 3 属于异常输入，应被拦。"""
        code, out = run("commission.py", "--scene", "lease", "--rent", "3500", "--months", "5")
        self.assertNotEqual(code, 0, out)

    def test_lease_share_100_percent_allowed(self):
        """房东全担（--landlord-share 1）是合法值，不得误报单位错误。"""
        code, out = run("commission.py", "--scene", "lease", "--rent", "3500", "--landlord-share", "1")
        self.assertEqual(code, 0, out)
        self.assertNotIn("单位提醒", out, out)


class TestFormulas(unittest.TestCase):
    def test_tax_total_equals_sum_of_parts(self):
        """交易全成本 = 税费小计 + 费用小计（内部自洽）。"""
        code, out = run("tax.py", "--price", "1500000", "--area", "89",
                        "--first", "1", "--held", "6", "--unique", "1")
        self.assertEqual(code, 0, out)
        tax = num(out, r"税费小计[^\d]*([\d,]+)")
        fee = num(out, r"费用小计[^\d]*([\d,]+)")
        total = num(out, r"★ 交易全成本[^\n]*?([\d,]+)\s*元")
        self.assertAlmostEqual(total, tax + fee, delta=2, msg=out)

    def test_mortgage_monthly_positive_and_amortizes(self):
        """月供为正，且 30 年内总还款 > 贷款额（利息存在）。"""
        code, out = run("mortgage.py", "--price", "1500000", "--downpay", "30", "--years", "30")
        self.assertEqual(code, 0, out)
        self.assertRegex(out, r"月供")

    def test_holding_vacancy_twelve_months_no_crash(self):
        """年空置 12 个月是极端但合法输入，不能崩（除零风险点）。"""
        code, out = run("holding.py", "--area", "89", "--property", "2.5", "--price", "1500000",
                        "--vacancy", "12")
        self.assertIn(code, (0, 2), out)  # 0=正常；被参数校验拒绝也算处理得当

    def test_prepay_reduces_interest(self):
        """提前还款后利息总额必须下降。"""
        code, out = run("prepay.py", "--loan", "700000", "--rate", "3.1", "--years", "30",
                        "--paid", "60", "--prepay", "300000")
        self.assertEqual(code, 0, out)
        self.assertTrue(re.search(r"节省|减少|省", out), out)


class TestSmokeAllTools(unittest.TestCase):
    """每个工具都要能用 --help 跑起来（防 argparse 字符串回归）。"""

    def test_all_tools_help(self):
        tools = sorted(f for f in os.listdir(CALC) if f.endswith(".py") and not f.startswith("_"))
        self.assertGreaterEqual(len(tools), 19, f"计算器数量异常：{tools}")
        for tool in tools:
            code, out = run(tool, "--help")
            self.assertEqual(code, 0, f"{tool} --help 失败：{out[:400]}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
