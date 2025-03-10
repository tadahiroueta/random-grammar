class Symbol:
    def __init__(self, value: str | None):
        self.value = value

class TerminalSymbol(Symbol):
    def __init__(self, value: str):
        super().__init__(value)

class VariableSymbol(Symbol):
    def __init__(self, name: str):
        self.name = name
        super().__init__(None)