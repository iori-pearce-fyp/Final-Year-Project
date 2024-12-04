import visualisation_utils
from OneLimitedAutomata import OneLimitedAutomata

states = ["q_0", "q_1", "q_2"]
input_alphabet = ["a", "b"]
transition_function = "q_0 a.X +1 q_1,q_1 a.X +1 q_1,q_1 b.X +1 q_2,q_2 b.X +1 q_2,q_2 >.> +1 q_2"
initial_state = "q_0"
accepting_states = ["q_2"]


try:
    la = OneLimitedAutomata()
    la.input_states(states)
    la.input_input_alphabet(input_alphabet)
    # la.add_tape_alphabet_characters([("X", "overwrite")])
    la.input_transition_function(transition_function)
    la.input_initial_state(initial_state)
    la.input_accepting_states(accepting_states)
except ValueError as e:
    print("Issue with object creation: ", {e})

visualisation_utils.produce_la_visual_representation(la)