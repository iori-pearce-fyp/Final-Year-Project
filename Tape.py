from TapeSymbol import TapeSymbol

class Tape:
    def __init__(self, input_word):
        self.tape = [TapeSymbol("<", "endpoint"), list(input_word), TapeSymbol(">", "endpoint")]
        
    
    # Implement functions to update tape at later date