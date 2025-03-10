import unittest

from classes.option import Option
from classes.symbol import TerminalSymbol, VariableSymbol


class TestOption(unittest.TestCase):
    def test_option(self):
        WEIGHT = 1
        VALUE = [
            TerminalSymbol('a'),
            VariableSymbol('b'),
            TerminalSymbol('c'),
        ]

        option = Option(WEIGHT, VALUE)

        self.assertEqual(option.weight, WEIGHT, 'Failed to set weight')
        self.assertEqual(option.value, VALUE, 'Failed to set value')

if __name__ == '__main__':
    unittest.main()