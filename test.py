from OneLimitedAutomata import OneLimitedAutomata

states = ["q_0", "q_1", "q_2"]
input_alphabet = ["a", "b"]
transition_function = "q_0 a.X +1 q_1,q_1 a.X +1 q_1,q_1 b.X +1 q_2,q_2 b.X +1 q_2,q_2 >.> +1 q_2"
initial_state = "q_0"
accepting_states = ["q_2"]


try:
    new_automata = OneLimitedAutomata(states, input_alphabet, transition_function, initial_state, accepting_states)
    new_automata.return_details()
except ValueError as e:
    print("Issue with object creation: ", {e})

