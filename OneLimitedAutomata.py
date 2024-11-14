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
    
    def __init__(self, states, input_alphabet, transition_function, initial_state, accepting_states):
        self.halted = False
        self.tape = [TapeSymbol("<"), TapeSymbol(">")]
        self.tape_alphabet = []
        self.current_state = "" 
    
        # Head position always set to 1. 
        # N.B. 0 is "<" symbol of the tape
        self.head_position = 1

        # Methods to validate the inputs of the class
        self.states = self.validate_states(states)
        self.input_alphabet = self.validate_input_alphabet(input_alphabet)
        self.tape_alphabet = self.create_tape_alphabet(input_alphabet)
        self.initial_state = self.validate_initial_state(initial_state)
        self.accepting_states = self.validate_accepting_states(accepting_states)
        self.transition_function = self.validate_transition_function(transition_function) 
        
        self.set_current_state(initial_state)


    """
    Function that ensures the input states are valid according to the following:
    - A list
    - Each element of the list is a string
    """
    def validate_states(self, states):
        if not isinstance(states, list):
            raise ValueError("States are not of type list")
        
        for state in states:
            if not isinstance(state, str):
                raise ValueError(f"State {state} is not of type str")

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
                raise ValueError(f"{char} is not a single-character string.")
        
        formatted_input_alphabet = list(set(input_alphabet))
        
        return formatted_input_alphabet


    """
    Function that takes as input the input_alphabet
    Creates the three additional tape symbols using the TapeSymbol class
    Adds the additional tape symbols to the original input_alphabet and returns this final list
    """
    def create_tape_alphabet(self, input_alphabet):
        overwrite_symbol = TapeSymbol("X")
        left_endpoint_symbol = TapeSymbol("<")
        right_endpoint_symbol = TapeSymbol(">")

        tape_alphabet = input_alphabet + [overwrite_symbol, left_endpoint_symbol, right_endpoint_symbol]

        return tape_alphabet


    """
    Function that ensures the initial state is in the set of states
    Return the initial_state if valid
    Otherwise, raises an error
    """
    def validate_initial_state(self, initial_state):
        if initial_state in self.states:
            return initial_state
        else:
            raise ValueError("Initial state not in set of states.")

    
    """
    Function that checks if each state in the accepting_states is in the set of states
    Returns the accepting_states if all valid
    Otherwise, raises an error
    """
    def validate_accepting_states(self, accepting_states):
        for state in accepting_states:
            if state not in self.states:
                raise ValueError(f"Accepting state {state} is not in set of states.")
        
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
            except ValueError as e:
                raise ValueError(f"Issue with input of transition function string. Ensure structure is as required")

            # Run checks on each part of the transition
            if read_state not in self.states:
                raise ValueError(f"State {read_state} is not in set of states.")
            if alphabet_char not in self.tape_alphabet and alphabet_char not in [tape_symbol.symbol for tape_symbol in self.tape_alphabet if isinstance(tape_symbol, TapeSymbol)]:
                raise ValueError(f"Alphabet character {alphabet_char} not in tape alphabet.")
            if rewrite not in [tape_symbol.symbol for tape_symbol in self.tape_alphabet if isinstance(tape_symbol, TapeSymbol)]:
                raise ValueError(f"Rewrite symbol {rewrite} is not in the tape alphabet.")
            if movement not in ["0", "+1", "-1"]:
                raise ValueError(f"Movement symbol {movement} is not in the valid moves.")
            if resultant_state not in self.states:
                raise ValueError(f"Resultant state {resultant_state} is not in the valid set of states.")

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
    Function that returns information about the limited automata
    """
    def return_details(self):
        print(f"""Details of one limited automata:\n\nTape alphabet: {self.tape_alphabet}\nStates: {self.states}\nCurrent state: {self.current_state}\nTransition function: {self.transition_function}\nAccepting states: {self.accepting_states}\nHalted: {self.halted}\nHead position: {self.head_position}
        """)
                