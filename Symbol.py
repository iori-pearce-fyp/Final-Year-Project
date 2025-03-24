class Symbol:
    def __init__(self, symbol, marked=False):
        self.symbol = symbol
        self.marked = marked

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.symbol == other.symbol
        return False


    """
    Function that returns the hash of the symbol
    """
    def __hash__(self):
        return hash(self.symbol)
    

    """
    Function that returns string representation of the object
    """
    def __str__(self):
        return self.symbol