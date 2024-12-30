class Symbol:
    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, value):
        if isinstance(value, Symbol):
            return self.symbol == value.symbol
        return False

    def __hash__(self):
        return hash(self.symbol)
    
    def __str__(self):
        return f"Symbol: {self.symbol}"