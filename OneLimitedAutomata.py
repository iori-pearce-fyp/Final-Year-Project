from Tape import Tape
from TapeSymbol import TapeSymbol

"""
Class to create the base one limited automata

Parameters:
# states (Q) - finite set of states
# current_state - current state of the machine
# input_alphabet (Σ) - finite input alphabet
# tape_alphabet (Γ) - finite working alphabet
# transition_function (δ) - deterministic transition function
# initial_state (q_0) - initial state (q_0 ∈ Q)
# accepting_states (F) - set of final states
# head_position - keeps track of where the machine is currently reading from
# tape - the tape of the limited automata, represented using a list. Initialised with just end symbols
# halted - a boolean that determines whether the automata is halted or not
"""
class OneLimitedAutomata:
    
    def __init__(self):
        self.halted = False

        # self.transition_function = self.validate_transition_function(transition_function)
    

    """
    Function to input states to the limited automata
    Will validate the states then assign the states to the LA if valid
    """
    def input_states(self, states):
        self.validate_states(states)

        # Only assigned if no value error raised from above validation
        self.states = states
    

    """
    Function to input input alphabet to the limited automata
    Will validate the alphabet then assign the alphabet to the LA if valid
    Also produces the tape_alphabet if valid
    """
    def input_input_alphabet(self, input_alphabet):
        self.validate_input_alphabet(input_alphabet)

        # Only assigned if no value error raised from above validation
        self.input_alphabet = input_alphabet

        self.tape_alphabet = self.create_tape_alphabet(input_alphabet)

    
    """
    Function to input initial state to the limited automata
    Will validate the state then assign the initial state to the LA if valid
    """
    def input_initial_state(self, state):
        # Only assigned if no value error raised from validation method
        self.initial_state = state

    
    """
    Function to input accepting states to the limited automata
    Will validate the states then assign the accepting states to the LA if valid
    """
    def input_accepting_states(self, states):
        # Only assigned if no value error raised from validation function
        self.accepting_states = states

    
    """
    Function to input transition function to the limited automata
    Will validate the transition function then assign the to the LA if valid
    """
    def input_transition_function(self, transition_function):
        self.transition_function = transition_function


    """
    Function that ensures the input states are valid according to the following:
    - A set
    """
    def validate_states(self, states):
        if not isinstance(states, set):
            raise ValueError("States are not of type set")

        return states
        
  
    """
    Function that ensures that the input_alphabet is valid according to the following criteria:
    - a list of single character strings
    - no repeats of characters
    Returns the list if valid
    """
    def validate_input_alphabet(self, input_alphabet):
        for char in input_alphabet:
            if not (isinstance(char, str) and len(char) == 1):
                raise ValueError(f"{char} is not a single-character string")
        
        formatted_input_alphabet = set(input_alphabet)
        
        return formatted_input_alphabet


    """
    Function that takes as input the input_alphabet
    Creates the three additional tape symbols using the TapeSymbol class
    Adds the additional tape symbols to the original input_alphabet and returns this final list
    """
    def create_tape_alphabet(self, input_alphabet):
        return {TapeSymbol("<", "endpoint"), TapeSymbol(">", "endpoint"), *input_alphabet}
    

    """
    Function that will allow user to add unique characters to the tape alphabet
    Takes as input a list of chars and inserts them to the set, tape_alphabet
    """
    def add_tape_alphabet_characters(self, new_characters):
        for char, name in new_characters:
            if char not in [tape_symbol.symbol for tape_symbol in self.tape_alphabet if isinstance(tape_symbol, TapeSymbol)]:
                self.tape_alphabet.add(TapeSymbol(char, name))


    """
    Function that ensures the initial state is in the set of states
    Return the initial_state if valid
    Otherwise, raises an error
    """
    def validate_initial_state(self, initial_state):
        if initial_state in self.states:
            return initial_state
        else:
            return "initial_state_error"

    
    """
    Function that checks if each state in the accepting_states is in the set of states
    Returns the accepting_states if all valid
    Otherwise, raises an error
    """
    def validate_accepting_states(self, accepting_states):
        for state in accepting_states:
            if state not in self.states:
                return "accepting_state_error"
        
        return accepting_states


    """
    Function that takes as input the transition function string input.
    Determines if the input is valid according to the following format:
    "state<space>alphabet_char.rewrite_tape_symbol<space>movement<space>state,"
    If valid, the function will return the completed transition_function dictionary
    Otherwise the function will return an error
    """
    def validate_transition_function(self, transition_function):
        transitions = transition_function.split(",")
        resultant_transition_function = {}

        for transition in transitions:
            current_transition = transition.split(".")

            try:
                read_state, alphabet_char = current_transition[0].split(" ")
                rewrite, movement, resultant_state = current_transition[1].split(" ")
            except ValueError:
                print("HI")
                return "transition_input_error"

            # Run checks on each part of the transition
            if read_state not in self.states:
                return "state_input_error"
            if alphabet_char not in self.input_alphabet and alphabet_char not in {tape_symbol.symbol for tape_symbol in self.tape_alphabet if isinstance(tape_symbol, TapeSymbol)}:
                return "char_input_error"
            if rewrite not in self.tape_alphabet and rewrite not in {tape_symbol.symbol for tape_symbol in self.tape_alphabet if isinstance(tape_symbol, TapeSymbol)}:
                return "char_input_error"
            if movement not in ["0", "+1", "-1"]:
                return "movement_input_error"
            if resultant_state not in self.states:
                return "state_input_error"

            # Use read_state and alphabet_char as the key for transition function dictionary
            resultant_transition_function[(read_state, alphabet_char)] = (rewrite, movement, resultant_state)
        
        return resultant_transition_function

    
    """
    Function that sets the current state
    Called on instantiation of the object to the initial_state
    """
    def set_current_state(self, state):
        self.current_state = state


    """
    Function that creates the tape
    Loads the input word onto the tape as well as the left and right endpoint markers
    Initialises the head position to 1
    """
    def create_tape(self, input_word):
        if not isinstance(input_word, str):
            raise ValueError("Invalid format for input word")
        else:
            self.tape = Tape(input_word)

            # Head position always set to 1. 
            # N.B. 0 is "<" symbol of the tape
            self.head_position = 1


    """
    Function that accepts an input word
    Will call methods to initialise the tape and current state
    """
    def load_input_word(self, input_word):
        self.create_tape(input_word)

        self.set_current_state(self.initial_state)
            

    """
    Function that returns information about the limited automata, including dynamically added attributes
    """
    def return_details(self):
        return {key: value for key, value in self.__dict__.items()}
                