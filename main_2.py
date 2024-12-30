import visualisation_utils
from OneLimitedAutomata import OneLimitedAutomata
from State import State
from InputSymbol import InputSymbol

# VALID TEST INPUT
states = {"q_0", "q_1", "q_2"}
input_alphabet = ["a", "b"]
initial_state = "q_0"
accepting_states = ["q_2"] 
transition_function = "q_0 a.X +1 q_1,q_1 a.X +1 q_1,q_1 b.X +1 q_2,q_2 b.X +1 q_2,q_2 >.> +1 q_2"

import sys

# def main(*args):
#     # Parse arguments from command line
#     if len(args) < 5:
#         print("Usage: main.py <states> <input_alphabet> <initial_state> <accepting_states> <transition_function>")
#         sys.exit(1)

#     states = args[0].split(",")
#     input_alphabet = args[1].split(",")
#     initial_state = args[2]
#     accepting_states = args[3].split(",")
#     transition_function = args[4]

#     automata = OneLimitedAutomata()
#     automata.input_states(states)
#     automata.input_input_alphabet(input_alphabet)
#     automata.input_initial_state(initial_state)
#     automata.input_accepting_states(accepting_states)
#     automata.input_transition_function(transition_function)

#     # Print to confirm parsing
#     print(f"States: {automata.states}")
#     print(f"Input Alphabet: {automata.input_alphabet}")
#     print(f"Initial State: {automata.initial_state}")
#     print(f"Accepting States: {automata.accepting_states}")
#     print(f"Transition Function: {automata.transition_function}")
#     print(f"Tape Alphabet: {automata.tape_alphabet}")

#     print("One Limited Automata created successfully!")

# def process_inputs():
#     print("Enter your inputs (Ctrl+C to stop) (help to see available commands):")
#     for line in sys.stdin:
#         line = line.strip()
#         if line:
#             print(f"Processing input: {line}")

#             if line == "help".lower():
#                 print("Options are:\nexecute <input_word>\nexecute_one_step\ndetails")
#         else:
#             print("Received an empty input, ignoring.")

# if __name__ == "__main__":
#     # Pass command line arguments to main
#     main(*sys.argv[1:])
#     process_inputs()

automata = OneLimitedAutomata()
automata.input_states(states)
automata.input_input_alphabet(input_alphabet)
automata.input_initial_state(initial_state)
automata.input_accepting_states(accepting_states)
automata.input_transition_function(transition_function)

print(automata.execute("<aabbabababbbabababbababab", False))