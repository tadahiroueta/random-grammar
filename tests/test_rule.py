import random
import unittest
from typing import Dict

from classes.rule import Rule
from classes.option import Option
from classes.symbol import TerminalSymbol, VariableSymbol


class TestRule(unittest.TestCase):
    NAME = VariableSymbol("Name")
    OPTIONS = {
        Option(1, [TerminalSymbol("Value1")]),
        Option(2, [TerminalSymbol("Value2")]),
        Option(3, [TerminalSymbol("Value3")]),
        Option(4, [TerminalSymbol("Value4")])
    }
    DELTA = 50

    @classmethod
    def setUpClass(cls):
        random.seed(0)

    def setUp(self):
        self.rule = Rule(TestRule.NAME, TestRule.OPTIONS)

    def test_initiate_rule(self):
        self.assertEqual(self.rule.name, self.NAME, "Failed to set name")

    def test_random_selection(self):
        selection_counts: Dict[str, int] = {}

        for _ in range(1000):
            selection = self.rule()
            value = selection[0].value

            if value not in selection_counts:
                selection_counts[value] = 0

            selection_counts[value] += 1

        self.assertAlmostEqual(selection_counts["Value1"], 100, delta=TestRule.DELTA,
                               msg="Failed to select proportionally.")
        self.assertAlmostEqual(selection_counts["Value2"], 200, delta=TestRule.DELTA,
                               msg="Failed to select proportionally.")
        self.assertAlmostEqual(selection_counts["Value3"], 300, delta=TestRule.DELTA,
                               msg="Failed to select proportionally.")
        self.assertAlmostEqual(selection_counts["Value4"], 400, delta=TestRule.DELTA,
                               msg="Failed to select proportionally.")

if __name__ == '__main__':
    unittest.main()