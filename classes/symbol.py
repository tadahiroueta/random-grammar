class Symbol:
    pass

class TerminalSymbol(Symbol):
    def __init__(self, value: str):
        self.value = value

class VariableSymbol(Symbol):
    def __init__(self, name: str):
        self.name = name