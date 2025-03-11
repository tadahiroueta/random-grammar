# project4.py
#
# ICS 33 Winter 2025
# Project 4: Still Looking for Something
from typing import Set, List

from classes.rule import Rule
from classes.option import Option
from classes.grammar import Grammar
from classes.symbol import TerminalSymbol, VariableSymbol


def parse_grammar(path: str) -> Grammar:
    rules: Set[Rule] = set()

    with open(path, 'r') as file:
        line = file.readline()
        while line:

            # start of rule
            if line == "{\n":
                name = file.readline().strip()
                options: List[Option] = []

                # end of rule
                line = file.readline().strip()
                while line != "}":

                    # options
                    weight, *value = line.split()
                    weight = int(weight)
                    value = [TerminalSymbol(symbol) if "[" in symbol else VariableSymbol(symbol)
                             for symbol in value]
                    options.append(Option(weight, value))

                    line = file.readline().strip()

                rules.add(Rule(name, options))

            line = file.readline()

    return Grammar(rules)

def main() -> None:
    grammar_file_path = input()
    number_of_sentences = int(input())
    start_variable_name = input()

    with open(grammar_file_path, 'r') as file:
        grammar = file.read()


if __name__ == '__main__':
    main()