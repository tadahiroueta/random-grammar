from typing import List, Generator

from classes.symbol import Symbol


class Option:
    def __init__(self, weight: int, value: List[Symbol]):
        self.weight = weight
        self.value = value

    def __call__(self) -> Generator[Symbol, None, None]:
        yield from self.value