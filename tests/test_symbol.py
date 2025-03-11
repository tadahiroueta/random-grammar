import unittest

from classes.symbol import TerminalSymbol, VariableSymbol

class TestSymbol(unittest.TestCase):
    def test_terminal_symbol(self):
        symbol = TerminalSymbol('a')
        self.assertEqual(symbol.value, 'a', 'Failed to create terminal symbol')

    def test_variable_symbol(self):
        symbol = VariableSymbol('A')
        self.assertEqual(symbol.name, 'A', 'Failed to create variable symbol')


if __name__ == '__main__':
    unittest.main()