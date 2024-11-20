import graphviz

"""
Function that will take as input a limited automata and plot the corresponding fsm diagram
"""
def produce_la_visual_representation(la):
    f = graphviz.Digraph('limited_automata', filename='la.gv')
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='circle')
    for node in set(la.states).difference(set(la.accepting_states)):
        f.node(f"{node}")

    f.attr('node', shape='doublecircle')
    for node in la.accepting_states:
        f.node(f"{node}")
    
    for (transition_key, transition_value) in la.transition_function.items():

        print(transition_key, transition_value)
        key_state = transition_key[0]
        key_char = transition_key[1]

        value_rewrite = transition_value[0]
        value_movement = transition_value[1]
        value_state = transition_value[2]

        f.edge(key_state, value_state, label=f"{key_char}/{value_rewrite},{value_movement}")

    f.view()