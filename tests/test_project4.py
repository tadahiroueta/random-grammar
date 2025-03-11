import io
import unittest
import contextlib
from random import seed
from unittest.mock import patch

from project4 import parse_grammar, main
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
            self.assertIsInstance(parsed._options[0]._value[0], TerminalSymbol,
                                  "Failed to parse the correct symbol type.")

    @patch('builtins.input', side_effect=["..\\data\\small.txt", "1000", "HowIsBoo"])
    def test_main(self, mock_input):
        POSSIBILITY_PROPORTIONS = {
            "Boo is happy today": 0.3,
            "Boo is perfect today": 0.3,
            "Boo is relaxing today": 0.1,
            "Boo is fulfilled today": 0.1,
            "Boo is excited today": 0.2
        }
        SEED = 0

        seed(SEED)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            main()

        sentences = output.getvalue().split("\n")[:-1]

        self.assertEqual(len(sentences), 1000,
                         "Failed to generate the correct number of sentences.")
        for sentence in sentences:
            self.assertIn(sentence, POSSIBILITY_PROPORTIONS.keys(),
                          "Failed to generate a valid sentence.")

        for possibility, proportion in POSSIBILITY_PROPORTIONS.items():
            self.assertAlmostEqual(sentences.count(possibility) / 1000, proportion, places=1,
                                   msg="Failed to generate the correct proportion of sentences.")


if __name__ == '__main__':
    unittest.main()