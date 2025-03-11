import unittest
from random import seed
from typing import Dict

from classes.rule import Rule
from classes.option import Option
from classes.symbol import TerminalSymbol, VariableSymbol


class TestRule(unittest.TestCase):

    def test_random_selection(self):
        SEED = 0
        NAME = VariableSymbol("Name")
        OPTIONS = [
            Option(1, [TerminalSymbol("Value1")]),
            Option(2, [TerminalSymbol("Value2")]),
            Option(3, [TerminalSymbol("Value3")]),
            Option(4, [TerminalSymbol("Value4")])
        ]
        DELTA = 50

        seed(SEED)
        rule = Rule(NAME, OPTIONS)

        selection_counts: Dict[str, int] = {}
        for _ in range(1000):
            selection = rule()
            value = "".join(symbol.value for symbol in selection)

            if value not in selection_counts:
                selection_counts[value] = 0

            selection_counts[value] += 1

        self.assertAlmostEqual(selection_counts["Value1"], 100, delta=DELTA,
                               msg="Failed to select proportionally.")
        self.assertAlmostEqual(selection_counts["Value2"], 200, delta=DELTA,
                               msg="Failed to select proportionally.")
        self.assertAlmostEqual(selection_counts["Value3"], 300, delta=DELTA,
                               msg="Failed to select proportionally.")
        self.assertAlmostEqual(selection_counts["Value4"], 400, delta=DELTA,
                               msg="Failed to select proportionally.")

if __name__ == '__main__':
    unittest.main()