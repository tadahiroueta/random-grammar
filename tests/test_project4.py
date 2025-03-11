import unittest

from project4 import parse_grammar
from classes.rule import Rule
from classes.option import Option
from classes.grammar import Grammar
from classes.symbol import TerminalSymbol, VariableSymbol


class TestProject4(unittest.TestCase):
    def test_parse_grammar(self):
        PATH = "..\\data\\small.txt"
        MODEL_GRAMMAR = Grammar({
            Rule("HowIsBoo", [Option(1, [
                TerminalSymbol("Boo"),
                TerminalSymbol("is"),
                VariableSymbol("Adjective"),
                TerminalSymbol("today")
            ])]),
            Rule("Adjective", [
                Option(3, [TerminalSymbol("happy")]),
                Option(3, [TerminalSymbol("perfect")]),
                Option(1, [TerminalSymbol("relaxing")]),
                Option(1, [TerminalSymbol("fulfilled")]),
                Option(2, [TerminalSymbol("excited")]),
            ])
        })

        parsed_grammar = parse_grammar(PATH)

        self.assertEqual(len(parsed_grammar._rules), len(MODEL_GRAMMAR._rules),
                         "Failed to parse the correct number of rules.")

        parsed_rule_values = list(parsed_grammar._rules.values())
        parsed_rule_values.sort(key=lambda rule: rule.name)

        model_rule_values = list(MODEL_GRAMMAR._rules.values())
        model_rule_values.sort(key=lambda rule: rule.name)

        for parsed, model in zip(parsed_rule_values, model_rule_values):
            self.assertEqual(parsed.name, model.name,
                             "Failed to parse the correct rule name.")
            self.assertEqual(len(parsed._options), len(model._options),
                             "Failed to parse the correct number of options.")
            self.assertEqual(len(parsed._options[0]._value),
                             len(model._options[0]._value),
                             "Failed to parse the correct number of symbols in an option.")


if __name__ == '__main__':
    unittest.main()