from State import State
from Symbol import Symbol
from InputSymbol import InputSymbol
from TapeSymbol import TapeSymbol
from Tape import Tape

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

class OneLimitedAutomata_rework:
    
    # Constructor function, used to initialise the machine
    def __init__(self, states = set(), initial_state = None, accepting_states = set(), sigma = set(), gamma = set(), delta = {}):
        # boolean variable used to track state of machine
        self.halted = False
        # transition function
        self.delta = {}
        # set of states of the machine
        self.states = set()
        # the initial state of the machine
        self.initial_state = None
        # set of accepting states of the machine
        self.accepting_states = set()
        # alphabet representing the input symbols
        self.sigma = set()
        # alphabet representing the tape symbols (note that the two end marker symbols are always initialised. Can add anything else on top of them)
        self.gamma = set([TapeSymbol("<"), TapeSymbol(">")])

        self.run_setup(states, initial_state, accepting_states, sigma, gamma, delta)
    
    def run_setup(self, states, initial_state, accepting_states, sigma, gamma, delta):
        self.add_states(states)
        self.add_initial_state(initial_state)
        self.add_accepting_states(accepting_states)
        self.add_input_symbols(sigma)
        self.add_tape_symbols(gamma)
        self.add_transitions(delta)
    
    

    ### HELPER FUNCTIONS

    # helper function that adds a new state to the machine's states variables
    def add_states(self, new_states):
        # convert raw state into a State object
        states = [State(new_state) for new_state in new_states]
        # add state, because the states variable is a set duplicates will not be added
        for state in states:
            self.states.add(state)
    
    # helper function that takes a list of states and removes them from the states list if valid
    def remove_states(self, states_to_remove):
        # convert raw format into State objects
        states = [State(state_to_remove) for state_to_remove in states_to_remove]
        # check if state is in the states variable and remove
        for state in states:
            if state in self.states:
                self.states.remove(state)

    # Function that adds a new initial state, it will overwrite the current initial state
    def add_initial_state(self, state):
        # convert raw state into a State object
        new_initial_state = State(state)
        # check if the state is in the set of states
        if new_initial_state in self.states:
            self.initial_state = new_initial_state

    # Function that removes the current initial state and sets the initial state to None
    def remove_initial_state(self):
            self.initial_state = None
    
    # Function that adds states to the accepting states variable
    # Will add any new states to both the states set and the accepting states set
    def add_accepting_states(self, accepting_states):
        # convert raw states into State objects
        states = [State(accepting_state) for accepting_state in accepting_states]
        # add states to both machine's states and accepting_states variable (set prevents duplicates)
        for state in states:
            self.states.add(state)
            self.accepting_states.add(state)
    

    def add_input_symbols(self, input_symbols):
        # convert raw symbols into InputSymbol objects
        symbols = [InputSymbol(input_symbol) for input_symbol in input_symbols]
        # add each symbol to the machine's sigma variable
        for symbol in symbols:
            # check that the symbol is not already being used in the other alphabet
            if symbol not in self.gamma:
                self.sigma.add(symbol)
    
    def add_tape_symbols(self, tape_symbols):
        # convert raw symbols into InputSymbol objects
        symbols = [TapeSymbol(tape_symbol) for tape_symbol in tape_symbols]
        # add each symbol to the machine's sigma variable
        for symbol in symbols:
            # check that the symbol is not already being used in the other alphabet
            if symbol not in self.delta:
                self.gamma.add(symbol)

    def remove_input_symbols(self, input_symbols):
        # convert raw symbols into InputSymbol objects
        symbols = [InputSymbol(input_symbol) for input_symbol in input_symbols]
        # add each symbol to the machine's sigma variable
        for symbol in symbols:
            self.sigma.remove(symbol)

    def remove_tape_symbols(self, tape_symbols):
        # convert raw symbols into InputSymbol objects
        symbols = [TapeSymbol(tape_symbol) for tape_symbol in tape_symbols]
        # add each symbol to the machine's sigma variable
        for symbol in symbols:
            self.gamma.remove(symbol)


    # Code lifted from https://www.dcc.fc.up.pt/~rvr/FAdoDoc/_modules/FAdo/fa.html#DFA.addTransition
    # def addTransition(self, sti1, sym, sti2):
    #     """Adds a new transition from sti1 to sti2 consuming symbol sym.

    #     Args:
    #         sti1 (int): state index of departure
    #         sti2 (int): state index of arrival
    #         sym (Any): symbol consumed
    #     Raises:
    #         DFAnotNFA: if one tries to add a non-deterministic transition"""
    #     if sym == Epsilon:
    #         raise DFAnotNFA("Invalid Epsilon transition from {0:>s} to {1:>s}.".format(str(sti1), str(sti2)))
    #     self.Sigma.add(sym)
    #     if sti1 not in self.delta:
    #         self.delta[sti1] = {sym: sti2}
    #     else:
    #         if sym in self.delta[sti1] and self.delta[sti1][sym] is not sti2:
    #             raise DFAnotNFA("extra transition from ({0:>s}, {1:>s})".format(str(sti1), sym))
    #         self.delta[sti1][sym] = sti2

    def add_transitions(self, transitions):
        for transition in transitions:
            departure_state, symbol, arrival_state, rewrite_symbol, direction = transition
            self.add_transition(departure_state, symbol, arrival_state, rewrite_symbol, direction) 


    def add_transition(self, departure_state, symbol, arrival_state, rewrite_symbol, direction):
        # check that the direction is valid
        if self.check_valid_direction(direction):
            # check that the states involved are in the machine's set of states otherwise reject
            if self.check_valid_states([departure_state, arrival_state]):
                # check that the symbol involved exists
                if self.check_valid_symbol(symbol):
                    # Get the 0 or 1 value that represents whether the symbol is of type InputSymbol (0) or type TapeSymbol (1)
                    symbol_type = self.get_symbol_type(symbol)
                    # check if the departure_state and symbol tuple does not already exist in the transition function to ensure non-deterministic behaviour is not allowed
                    if ((State(departure_state), Symbol(symbol))) not in self.delta:
                        if symbol_type == "sigma":
                            self.delta[(State(departure_state), InputSymbol(symbol))] = (State(arrival_state), TapeSymbol(rewrite_symbol), direction)
                        elif symbol_type == "gamma":
                            self.delta[(State(departure_state), TapeSymbol(symbol))] = (State(arrival_state), TapeSymbol(rewrite_symbol), direction)
                    else:
                        print(f"Attempted new transition: ({departure_state}, {symbol}) violates non-determinism of the machine")
                else:
                    print("Symbols must be included in the machine's set of symbols before they can be use in transitions")
            else:
                print(f"States, {departure_state}, {arrival_state} must be included in the machine's set of states before they can be used in transitions")
        
    # function that removes a transition if it exists in the transition function
    def remove_transition(self, departure_state, symbol):
        # discard function on sets will not raise an error if the key is not found
        self.delta.pop((State(departure_state), Symbol(symbol)), None)
    

    def get_symbol_type(self, symbol_to_validate):
        symbol = Symbol(symbol_to_validate) 
        # loop through each of the tape and input symbols and return symbol type
        if symbol in self.sigma:
            return "sigma" 
        else:
            return "gamma"
        
    # function used to initialise the tape and must occur before processing (can be resued with new input words)
    def set_tape(self, input_word):
        # convert raw input to list of InputSymbols
        converted_input_word = [InputSymbol(char) for char in input_word]
        # create the tape using the converted_input_word
        self.tape = Tape(converted_input_word)
        # set the head_position to the index of the first non end-marker symbol on the tape (***assuming this is 1***)
        # ASK
        self.head = 1
        # set the current state to the initial state
        # ASK 
        self.current_state = self.initial_state

    # function that is only run once initialise tape is run otherwise returns error that tape has not been created yet with input word
    def execute(self):
        # check to see if input word has been used to initialise tape
        if not hasattr(self, "tape"):
            print("Need to initialise tape with an input word. Use the function set_tape(input_word) to do so")
        else:
            # while the machine has not halted
            while(not self.halted):
                # if the index of the head has not exceeded the tape length
                if self.head != len(self.tape.tape):
                    # assign the currently being read symbol to the variable symbol_reading
                    symbol_reading = self.tape.tape[self.head]
                    # if there exists a valid transition in the transition function
                    if ((self.current_state, symbol_reading)) in self.delta:
                        # get the values for the three below parameters from the transition function dictionary
                        arrival_state, overwrite_symbol, direction = self.delta[(self.current_state, symbol_reading)]

                        # update the current state to the arrival_state
                        self.current_state = arrival_state

                        # rewrite the symbol on the tape
                        self.tape.tape[self.head] = overwrite_symbol

                        # move the head in the correct direction
                        self.head += direction
                    # otherwise there does not exist a valid transition so we should halt the machine
                    else:
                        self.halted = True
                else:
                    # otherwise we have gone beyond the right end marker and should halt the machine
                    self.halted = True
        print(self.tape.return_tape())
        # do final check to see if machine has halted in an accepting state
        if self.halted and self.current_state in self.accepting_states:
            return True
        else:
            return False




    ### VALIDATION FUNCTIONS

    def check_valid_states(self, states_to_validate):
        # convert raw format to State objects
        states = [State(state_to_validate) for state_to_validate in states_to_validate]
        # loop through each state and see if it exists in the machine's set of states
        for state in states:
            if state not in self.states:
                return False
        return True
    
    def check_valid_symbol(self, symbol_to_validate):
        symbol = Symbol(symbol_to_validate) 
        # loop through each of the tape and input symbols and return true if in either or false otherwise
        if symbol in self.sigma or symbol in self.gamma:
            return True 
        else:
            return False
        
    def check_valid_direction(self, direction_to_validate):
        if direction_to_validate in [-1, 1]:
            return True
        else:
            return False


    # REPRESENTATION FUNCTIONS

    # function that returns the current set of states
    def return_states(self):
        states_string = "\n".join(str(state) for state in self.states)
        return states_string
    
    # function that returns the current initial state
    def return_initial_state(self):
        initial_state = str(self.initial_state)
        return initial_state
    
    # function that returns the current set of accepting_states
    def return_accepting_states(self):
        states_string = "\n".join(str(state) for state in self.accepting_states)
        return states_string
    
    # function that returns the current input alphabet (sigma)
    def return_sigma(self):
        symbols_string = "\n".join(str(symbol) for symbol in self.sigma)
        return symbols_string

    # function that returns the current tape alphabet (gamma)
    def return_gamma(self):
        symbols_string = "\n".join(str(symbol) for symbol in self.gamma)
        return symbols_string

    # functiont that returns the current tape alphabet (gamma)
    
    # function that returns the current transition function
    def return_transition_function(self):
        transitions_string = "\n".join(
            "(" + str(key[0]) + ", " + str(key[1]) + ") => (" + str(value[0]) + ", " + str(value[1]) + ", " + str(value[2]) + ")"
            for key, value in self.delta.items()
        )

        return transitions_string
    


###
# Need to SAFELY remove states, so that the transitions are also removed