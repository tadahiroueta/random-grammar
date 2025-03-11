from random import choices
from typing import List, Generator

from classes.option import Option
from classes.symbol import Symbol, VariableSymbol


class Rule:
    def __init__(self, name: VariableSymbol, options: List[Option]):
        self.name = name
        self._options = options
        self._option_weights = [option.weight for option in options]

    def __call__(self) -> Generator[Symbol, None, None]:
        """Returns one of the options based on the weights."""
        yield from choices(self._options, self._option_weights, k=1)[0]()