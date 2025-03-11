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
        generator = option()

        self.assertEqual(option.weight, WEIGHT, 'Failed to set weight')
        self.assertEqual(option.value, VALUE, 'Failed to set value')
        self.assertEqual(next(generator), VALUE[0], 'Failed to yield first symbol')
        self.assertEqual(next(generator), VALUE[1], 'Failed to yield second symbol')
        self.assertEqual(next(generator), VALUE[2], 'Failed to yield third symbol')

if __name__ == '__main__':
    unittest.main()