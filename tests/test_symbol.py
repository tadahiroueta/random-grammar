import unittest

from classes.symbol import TerminalSymbol, VariableSymbol

class TestSymbol(unittest.TestCase):
    def test_terminal_symbol(self):
        symbol = TerminalSymbol('a')
        self.assertEqual(symbol.value, 'a', 'Failed to create TerminalSymbol')

    def test_variable_symbol(self):
        symbol = VariableSymbol('Name')
        self.assertEqual(symbol.name, 'Name', 'Failed to name VariableSymbol')
        self.assertEqual(symbol.value, None, 'Failed to assign no value to VariableSymbol')
        symbol.value = 'value'
        self.assertEqual(symbol.value, 'value', 'Failed to assign value to VariableSymbol')


if __name__ == '__main__':
    unittest.main()