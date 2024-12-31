from TapeSymbol import TapeSymbol

class Tape:
    def __init__(self, input_word):
        self.tape = [TapeSymbol("<"), *input_word, TapeSymbol(">")]
        
    """
    Function that returns the tape and its contents in a presentable format
    """
    def output_tape(self):
        output_str = "["
        for symbol in self.tape:
            if isinstance(symbol, TapeSymbol):
                output_str += f"{symbol.symbol}, "
            else:
                output_str += f"{symbol}, " 
        return output_str.rstrip(", ") + "]"

    """
    Function that updates the tape
    Takes the following parameters:
    - index: Index position of the tape that needs updating
    - overwrite_char: Character that will be written at the index position
    """
    def update_tape(self, index, overwrite_char):
        self.tape[index] = overwrite_char