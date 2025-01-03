from Tape import Tape
from TapeSymbol import TapeSymbol
from InputSymbol import InputSymbol
from Symbol import Symbol
from State import State

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
    
    """
    Constructor, sets the halted attribute to False
    """
    def __init__(self):
        self.halted = False
    

    """
    Function to input states to the limited automata
    Will validate the states then assign the states to the LA if valid
    """
    def input_states(self, states):
        # Convert each raw state into a State object
        states = {State(state) for state in states}
        self.states = self.validate_states(states)
    

    """
    Function to input input alphabet to the limited automata
    Will validate the alphabet then assign the alphabet to the LA if valid
    Also produces the tape_alphabet if valid
    """
    def input_input_alphabet(self, input_alphabet):
        # Convert each raw input symbol into an InputSymbol object
        converted_input_alphabet = {InputSymbol(input_symbol) for input_symbol in input_alphabet}
        self.input_alphabet = self.validate_input_alphabet(converted_input_alphabet)

        self.tape_alphabet = self.create_tape_alphabet(self.input_alphabet)

    
    """
    Function to input initial state to the limited automata
    Will validate the state then assign the initial state to the LA if valid
    """
    def input_initial_state(self, state):
        # Convert raw state into a State object
        initial_state = State(state)
        self.initial_state = self.validate_initial_state(initial_state)

    
    """
    Function to input accepting states to the limited automata
    Will validate the states then assign the accepting states to the LA if valid
    """
    def input_accepting_states(self, states):
        # Convert each raw state into a State object
        converted_accepting_states = {State(state) for state in states}
        self.accepting_states = self.validate_accepting_states(converted_accepting_states)

    
    """
    Function to input transition function to the limited automata
    Will validate the transition function then assign the to the LA if valid
    """
    def input_transition_function(self, transition_function):
        self.transition_function = self.validate_transition_function(transition_function)


    """
    Function that ensures the input states are valid according to the following:
    - Of type State
    Returns the set of states if valid
    """
    @staticmethod
    def validate_states(states):
        for state in states:
            if not isinstance(state, State):
                raise ValueError("States are not of type State")

        return states
        
  
    """
    Function that ensures that the input_alphabet is valid according to the following criteria:
    - of type InputSymbol
    Returns the input alphabet if valid
    """
    @staticmethod
    def validate_input_alphabet(input_alphabet):
        for input_char in input_alphabet: 
            if not isinstance(input_char, InputSymbol):
                raise ValueError("Input states are not of type InputSymbol")

        return input_alphabet
    

    """
    Function that takes as input the input_alphabet
    Creates the three additional tape symbols using the TapeSymbol class
    Adds the additional tape symbols to the original input_alphabet and returns this final set
    """
    @staticmethod
    def create_tape_alphabet(input_alphabet):
        return {TapeSymbol("<"), TapeSymbol(">"), TapeSymbol("X"), *input_alphabet}
    

    """
    Function that allows addition of characters to the tape alphabet
    Takes as input a list of chars and inserts them to the set, tape_alphabet
    """
    def add_tape_alphabet_characters(self, new_characters):
        for char in new_characters:
            if TapeSymbol(char) not in {tape_symbol for tape_symbol in self.tape_alphabet if isinstance(tape_symbol, TapeSymbol)}:
                self.tape_alphabet.add(TapeSymbol(char))


    """
    Function that ensures the initial state is in the set of states
    Return the initial_state if valid
    Otherwise, raises an error
    """
    def validate_initial_state(self, initial_state):
        if initial_state in self.states and isinstance(initial_state, State):
            return initial_state
        else:
            raise ValueError("Initial state is not of type State")

    
    """
    Function that converts each raw input state to a state object
    Creates a set of these states
    Returns the accepting_states if the new set is a subset of the states parameter
    Otherwise, raises an error
    """
    def validate_accepting_states(self, accepting_states):
        # Check if the set of accepting states is a subset of self.states
        if accepting_states.issubset(self.states):
            return accepting_states  
        else:
            raise ValueError("Accepting states are not subset of states")


    """
    Function that takes as input the transition function string input.
    Determines if the input is valid according to the following format:
    "state<space>alphabet_char.rewrite_tape_symbol<space>movement<space>state,"
    If valid, the function will return the completed transition_function dictionary
    Otherwise the function will return an error
    """
    def validate_transition_function(self, transition_function):
        # Split the raw input into the separate transitions
        transitions = transition_function.split(",")
        # Create dictionary to store the processed transition function
        resultant_transition_function = {}

        for transition in transitions:
            # Split the raw transition into its components
            current_transition = transition.split(".")

            try:
                read_state, alphabet_char = current_transition[0].split(" ")
                rewrite, movement, resultant_state = current_transition[1].split(" ")
            except ValueError:
                return "transition_input_error"

            # Run checks on each part of the transition
            if State(read_state) not in self.states:
                raise ValueError("Read state not in the set of states")
            
            if Symbol(alphabet_char) not in self.tape_alphabet:
                raise ValueError("Alphabet character not in the tape alphabet")
            
            if Symbol(rewrite) not in self.tape_alphabet:
                raise ValueError("Rewrite symbol not in the tape alphabet")
            
            if int(movement) not in [0, +1, -1]:
                raise ValueError("Movement not in the accepted movements")
            
            if State(resultant_state) not in self.states:
                raise ValueError("Resultant state not in the set of states")

            # Use read_state and alphabet_char as the key for transition function dictionary
            resultant_transition_function[(State(read_state), Symbol(alphabet_char))] = (Symbol(rewrite), int(movement), State(resultant_state))
        
        return resultant_transition_function

    
    """
    Function that sets the current state
    """
    def set_current_state(self, state):
        self.current_state = state


    """
    Function that creates the tape
    Loads the input word onto the tape as well as the left and right endpoint markers
    Initialises the head position to 1
    """
    def create_tape(self, input_word):
        # Check that the input_word is a list of symbols before creating the tape
        if not all(isinstance(symbol, Symbol) for symbol in input_word):
            raise ValueError("Invalid format for input word")
        else:
            self.tape = Tape(input_word)

            # Head position always set to 1. 
            # N.B. 0 is "<" symbol of the tape
            self.head_position = 1
    

    """
    Function that will run the processing of the word on the 1LA
    Intialises the tape and the head position
    Executes the word on the automata
    Parameters:
    - input_word: a string that is run in the automata
    - one_step: a boolean parameter that executes one step if true otherwise runs the entire execution 
    """
    def execute(self, input_word, one_step):
        # If current state has not yet been instantiated, do so here (first run through) 
        if not hasattr(self, 'current_state'):
            self.set_current_state(self.initial_state)
        # If tape has not yet been instantiated, do so here (first run through)
        if not hasattr(self, 'tape'):
            converted_input_word = [InputSymbol(symbol) for symbol in input_word]
            self.create_tape(converted_input_word)

        if one_step:
            # Returns True if managed to execute one step successfully
            print(self.execute_one_step())
        else:
            # Run the whole execution of the word on the automaton
            not_recognised = False
            while self.halted != True:
                if not self.execute_one_step():
                    not_recognised = True
                    break
            if not_recognised:
                return False
            else:
                return True


    """
    Function that performs one step of the execution of the automaton
    Returns True if step performed successfully
    Returns False if step not able to be performed and hence word not accepted
    """
    def execute_one_step(self):
        if not self.transition_function.get((self.current_state, (self.tape.tape[self.head_position])), False):
            return False
        else:
            # before_step = self.generate_tape_visualisation("Before")

            # Get the three parts of the transition rule
            write_symbol, movement, new_state = self.transition_function.get((self.current_state, (self.tape.tape[self.head_position])), False)

            self.tape.update_tape(self.head_position, TapeSymbol(write_symbol))
            self.update_head_position(movement)
            self.set_current_state(new_state)

            if self.check_current_state_in_accepting_states() and self.head_position == len(self.tape) - 1:
                self.halted == True

            # after_step = self.generate_tape_visualisation("After")

            # print(before_step)
            # print(after_step)
            return True

    
    """
    Function that will run the whole execution of the word
    Returns True if the word is accepted and False otherwise
    Assume for now that the machine will not infinitely loop
    """
    def recognises(self, input_word):
        print(self.execute(input_word, False))


    """
    Helper function that checks if the current state is in the accepting states    
    """
    def check_current_state_in_accepting_states(self):
        if self.current_state in self.accepting_states:
            return True
        else:
            return False
        
        
    """
    Function to update the head position
    """
    def update_head_position(self, movement):
        if movement == 1:
            self.head_position += 1
        elif movement == -1:
            self.head_position -= 1
    

    """
    Function that creates and returns a string representation of the current state of the tape
    """
    def generate_tape_visualisation(self, condition):
        output_string = f"{condition} execution of step: | "
        for char in self.tape.tape:
            output_string += f"{char.symbol if isinstance(char, TapeSymbol) else char} | "
        return output_string.rstrip(" ")
        

    """
    Function that returns information about the limited automata, including dynamically added attributes
    """
    def return_details(self):
        return {key: value for key, value in self.__dict__.items()}
                