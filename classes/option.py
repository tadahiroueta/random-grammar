from typing import List, Generator

from classes.symbol import Symbol


class Option:
    def __init__(self, weight: int, value: List[Symbol]):
        self._weight = weight
        self._value = value

    def __call__(self) -> Generator[Symbol, None, None]:
        yield from self._value