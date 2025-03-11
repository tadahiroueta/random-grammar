import unittest

from classes.option import Option
from classes.rule import Rule
from classes.grammar import Grammar
from classes.symbol import VariableSymbol, TerminalSymbol


class TestGrammar(unittest.TestCase):
    def test_grammar(self):
        RULES = {
            Rule(VariableSymbol("Variable_1"), [Option(1, [VariableSymbol("Variable_2")])]),
            Rule(VariableSymbol("Variable_2"), [Option(1, [TerminalSymbol("Terminal_1")])])
        }

        grammar = Grammar(RULES)
        sentence = " ".join([value for value in grammar("Variable_1")])
        self.assertEqual(sentence, "Terminal_1", "Failed to generate the correct sentence.")

if __name__ == '__main__':
    unittest.main()