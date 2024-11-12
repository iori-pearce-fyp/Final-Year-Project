class TapeSymbol:
    def __init__(self, symbol):
        self.symbol = symbol
        self.symbol_type = self.check_symbol(symbol)
    
    def check_symbol(self, symbol):
        if symbol == "X":
            return "overwrite"
        else:
            return "endpoint"