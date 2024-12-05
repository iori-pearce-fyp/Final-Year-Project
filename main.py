import visualisation_utils
from OneLimitedAutomata import OneLimitedAutomata


# VALID TEST INPUT
states = {"q_0", "q_1", "q_2"}
input_alphabet = ["a", "b"]
transition_function = "q_0 a.X +1 q_1,q_1 a.X +1 q_1,q_1 b.X +1 q_2,q_2 b.X +1 q_2,q_2 >.> +1 q_2"
initial_state = "q_0"
accepting_states = ["q_2"] 


def main():
    print("Welcome to the CLI for the 1-LA class\n")

    """
    # Following code is used when user needs to input all details.
    For testing purposes, we plug in values for 1LA

    la = OneLimitedAutomata()

    # Collect inputs using the reusable function
    get_input_until_valid(get_states_input, la)
    get_input_until_valid(get_input_alphabet, la)

    # Add tape alphabet mandatory character
    la.add_tape_alphabet_characters([("X", "overwrite")])

    get_input_until_valid(get_transition_function, la)
    get_input_until_valid(get_initial_state, la)
    get_input_until_valid(get_accepting_states, la)
    """

    la = OneLimitedAutomata()
    la.input_states(states)
    la.input_input_alphabet(input_alphabet)
    la.add_tape_alphabet_characters([("X", "overwrite")])
    la.input_transition_function(la.validate_transition_function(transition_function))
    la.input_initial_state(initial_state)
    la.input_accepting_states(accepting_states)

    print("Here are the details of your 1LA")
    print(la.return_details())

    view_graph = input("View graphical representation of automata? Y/N: ")

    if view_graph == "Y":
        visualisation_utils.produce_la_visual_representation(la)

    get_input_until_valid(get_input_word, la)

    print(la.tape.output_tape())

    while True:
        # Prompt the user and check for exit condition
        user_input = input("Word ready for processing: Press enter to execute one step (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        # Execute one step of the process
        result = la.process_input_word()
        if result:
            print(result)
            break

    

"""
"""
def get_input_until_valid(input_function, la):
    proceed = False
    while not proceed:
        proceed = input_function(proceed, la)
    return proceed
        

"""
Function that gets the user's states input
Converts the states to a set
Sets the states of the 1LA to the set
"""
def get_states_input(proceed, la):
    states_input = input("Enter the states for your base 1-LA class (leave a space between each state): ")

    # Check that at least one state has been inputted
    if not states_input.strip():  # If the input is empty or only spaces
        states = {" "}
    else:
        states = set(states_input.split())

    print("You inputted the following states", states)
    
    proceed_input = input("If you are happy to proceed, enter Y: ")

    if proceed_input == "Y":
        proceed = True
        la.input_states(states)
    
    return proceed


"""
Function that gets the user's input alphabet
Converts the alphabet to a set
Sets the input alphabet of the 1LA to the set
"""
def get_input_alphabet(proceed, la):
    input_alphabet_input = input("Enter the input alphabet for your base 1-LA class (each character in your input will be part of the input alphabet): ")

    # Check that at least one alphabet symbol has been inputted
    if not input_alphabet_input.strip():  
        # If the input is empty or only spaces, just create one char
        input_alphabet = {" "}
    else:
        input_alphabet = set(input_alphabet_input)

    print("You inputted the following input alphabet", input_alphabet)
    
    proceed_input = input("If you are happy to proceed, enter Y: ")

    if proceed_input == "Y":
        proceed = True
        la.input_input_alphabet(input_alphabet)
    
    return proceed


"""
Function that takes as gets the user's transition function
Checks the transition function is valid
Sets the transition function of the 1LA to the formatted output transition function
"""
def get_transition_function(proceed, la):
    transition_function_input = input("Enter the transition function for your base 1-LA class\nTransition function should be of format\nstate<space>alphabet_char.rewrite_tape_symbol<space>movement<space>state,\n")

    validation_function_output = la.validate_transition_function(transition_function_input)

    if validation_function_output == "transition_input_error":
        print("Error with the input of your transition function, please try again")
    elif validation_function_output == "state_input_error":
        print("Error with the input of your states in the transition function, please try again")
    elif validation_function_output == "char_input_error":
        print("Error with one of the chars used in the transition function, please try again")
    elif validation_function_output == "movement_input_error":
        print("Error with one of the movements in your transition function, please try again")
    else:
        la.input_transition_function(validation_function_output)
        proceed = True
    
    return proceed


"""
"""
def get_initial_state(proceed, la): 
    initial_state_input = input("Enter the initial state for your base 1-LA class: ")

    validation_function_output = la.validate_initial_state(initial_state_input)

    if validation_function_output == "initial_state_error":
        print("Error with initial state, please try again")
    else:
        print("You inputted the following initial state", initial_state_input)
    
        proceed_input = input("If you are happy to proceed, enter Y: ")

        if proceed_input == "Y":
            proceed = True
            la.input_initial_state(initial_state_input)
    
    return proceed   


"""
"""
def get_accepting_states(proceed, la):
    accepting_states_input = set(input("Enter the accepting states for your base 1-LA class (states should be separated by a space): ").split())

    validation_function_output = la.validate_accepting_states(accepting_states_input)

    if validation_function_output == "accepting_state_error":
        print("Error with accepting state, please try again")
    else:
        print("You inputted the following accepting states", accepting_states_input)
    
        proceed_input = input("If you are happy to proceed, enter Y: ")

        if proceed_input == "Y":
            proceed = True
            la.input_accepting_states(accepting_states_input)
    
    return proceed 


def get_input_word(proceed, la):
    input_word = input("Please enter a word to be processed by the 1LA: ")

    if not la.validate_input_word(input_word):
        print("Word rejected as consists of characters not in the input alphabet of the 1LA")
    else:
        print("Your input word is: ", input_word)
        
        proceed_input = input("If you are happy to proceed, enter Y: ")
        if proceed_input == "Y":
                proceed = True
                la.load_input_word(input_word)
    
    return proceed 


if __name__ == "__main__":
    main()