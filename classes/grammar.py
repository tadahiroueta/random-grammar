from typing import Set, Dict, Generator

from classes.rule import Rule
from classes.symbol import TerminalSymbol, VariableSymbol


class Grammar:
    def __init__(self, rules: Set[Rule]):
        self._rules: Dict[str, Rule] = { rule.name: rule for rule in rules }

    def __call__(self, start_variable: str) -> Generator[str, None, None]:
        for symbol in self._rules[start_variable]():
            if isinstance(symbol, TerminalSymbol):
                yield symbol.value

            if isinstance(symbol, VariableSymbol):
                yield from self(symbol.name)