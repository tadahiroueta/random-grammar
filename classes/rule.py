from random import choices
from typing import Set, List

from classes.option import Option
from classes.symbol import Symbol, VariableSymbol


class Rule:
    def __init__(self, name: VariableSymbol, options: Set[Option]):
        self.name = name
        self._option_values = [option.value for option in options]
        self._option_weights = [option.weight for option in options]

    def __call__(self) -> List[Symbol]:
        """Returns one of the options based on the weights."""
        return choices(self._option_values, self._option_weights, k=1)[0]