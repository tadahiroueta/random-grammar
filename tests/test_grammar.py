import unittest

from classes.option import Option
from classes.rule import Rule
from classes.grammar import Grammar
from classes.symbol import VariableSymbol, TerminalSymbol


class TestGrammar(unittest.TestCase):
    def test_grammar(self):
        RULES = {
            Rule(VariableSymbol("Variable_1"), { Option(1, [TerminalSymbol("Terminal_1")]) }),
            Rule(VariableSymbol("Variable_2"), { Option(1, [TerminalSymbol("Terminal_2")]) })
        }

        grammar = Grammar(RULES)
        self.assertEqual(len(grammar.rules), len(RULES),
                         "Failed to initialize Grammar object with rules")

if __name__ == '__main__':
    unittest.main()