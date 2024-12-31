class Symbol:
    def __init__(self, symbol):
        self.symbol = symbol


    """
    Function that will see if a different Symbol object has the same symbol
    Returns True if they do and False otherwise
    """
    def __eq__(self, value):
        if isinstance(value, Symbol):
            return self.symbol == value.symbol
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
        return f"Symbol: {self.symbol}"