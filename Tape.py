from TapeSymbol import TapeSymbol

class Tape:
    def __init__(self, input_word):
        # input_word is a list of InputSymbols
        self.tape = [TapeSymbol(">"), *input_word, TapeSymbol("<")]
        
    """
    Function that returns the tape and its contents in a presentable format
    """
    def return_tape(self):
        output_str = "["
        for symbol in self.tape:
            output_str += str(symbol) 
        return output_str.rstrip(", ") + "]"

    """
    Function that updates the tape
    Takes the following parameters:
    - index: Index position of the tape that needs updating
    - overwrite_char: TapeSymbol to be written onto the tape
    """
    def update_tape(self, index, overwrite_symbol):
        self.tape[index] = overwrite_symbol