from typing import Set, Dict

from classes.rule import Rule

class Grammar:
    def __init__(self, rules: Set[Rule]):
        self.rules: Dict[str, Rule] = { rule.name.name: rule for rule in rules }