from OneLimitedAutomata_rework import OneLimitedAutomata_rework


# Below is the definition of a 1LA that accepts the language of words from the paper where n = 2 and the number of repeats is greater than 0

automaton = OneLimitedAutomata_rework(states=["q0", "0", "q1", "a1", "b1", "1", "q2", "q3", "a2", "b2", "2", "qe", "q4", "q5", "qf"], initial_state="q0", accepting_states=["qf"], sigma=["a", "b"], gamma=["X", "/", "a'", "b'"], delta=[("q0", "a", "0", "a'", 1), ("q0", "b", "0", "b'", 1), ("0", "a", "0", "a'", -1), ("0", "b", "0", "b'", -1), ("0", "a'", "0", "a'", -1), ("0", "b'", "0", "b'", -1), ("0", "/", "0", "/", -1), ("0", "X", "0", "X", -1), ("0", ">", "q1", ">", 1), ("q1", "a'", "a1", "a'", 1), ("q1", "b'", "b1", "b'", 1), ("a1", "/", "a1", "/", 1), ("a1", "X", "a1", "X", 1), ("a1", "a'", "a1", "a'", 1), ("a1", "b'", "a1", "b'", 1), ("b1", "/", "b1", "/", 1), ("b1", "X", "b1", "X", 1), ("b1", "a'", "b1", "a'", 1), ("b1", "b'", "b1", "b'", 1), ("b1", "a", "1", "X", -1), ("b1", "b", "1", "/", -1), ("a1", "a", "1", "/", -1), ("a1", "b", "1", "X", -1), ("1", "a'", "1", "a'", -1), ("1", "b'", "1", "b'", -1), ("1", "/", "1", "/", -1), ("1", "X", "1", "X", -1), ("1", ">", "q2", ">", 1), ("q2", "a'", "q3", "a'", 1), ("q2", "b'", "q3", "b'", 1), ("q3", "a'", "a2", "a'", 1), ("q3", "b'", "b2", "b'", 1), ("b2", "/", "b2", "/", 1), ("b2", "X", "b2", "X", 1), ("a2", "/", "a2", "/", 1), ("a2", "X", "a2", "X", 1), ("b2", "a", "2", "X", -1), ("b2", "b", "2", "/", -1), ("2", "/", "0", "/", -1), ("2", "X", "0", "X", -1), ("a2", "a", "2", "/", -1), ("a2", "b", "2", "X", -1), ("a1", "<", "qe", "<",-1), ("b1", "<", "qe", "<",-1), ("qe", "X", "q5", "X", -1), ("qe", "/", "q4", "/", -1), ("q5", "X", "qe", "X", -1), ("q5", "/", "qe", "/", -1), ("q4", "X", "qe", "X", -1), ("q4", "/", "qf", "/", 1), ("qf", "/", "qf", "/", 1), ("qf", "X", "qf", "X", 1), ("qf", "<", "qf", "<", 1)])

# print(automaton.return_states())

# print("\n")

# automaton.add_states(["q3"])

# print(automaton.return_states())

# automaton.remove_states(["q3", "q4"])

# print("\n")

# print(automaton.return_states())

# print(automaton.return_initial_state())

# print(automaton.return_states())
# print("\n")
# print(automaton.return_accepting_states())
# print("\n")
# automaton.remove_initial_state()
# print(automaton.return_initial_state())
# print("\n")
# automaton.add_initial_state("q2")


# automaton.set_tape("abbaab")
# print(automaton.tape.return_tape())

# automaton.set_tape("abbaba")
# print(automaton.tape.return_tape())

# print(automaton.execute())

# function that generates the transition function as well as all states required for the automaton
def generate_delta(n):
    delta = []
    tape_symbols = ["a'", "b'", "/", "X"]
    q_tracker = 0


    ### Scanning and marking the initial block
    # Scanning the initial n-1 chars
    for i in range(n-1):
        if i == n-2:
            delta.append((f"q{i}", "a", "0", "a'", 1))
            delta.append((f"q{i}", "b", "0", "b'", 1))
        else:
            delta.append((f"q{i}", "a", f"q{i + 1}", "a'", 1))
            delta.append((f"q{i}", "b", f"q{i + 1}", "b'", 1))
        q_tracker += 1
    
    # Add the nth char in the initial block
    delta.append(("0", "a", "0", "a'", -1))
    delta.append(("0", "b", "0", "b'", -1))

    ### Processing the nth char in the new block
    chars_processed_in_current_block_counter = 0

    # We have n repetitions of the general pattern observed in the DFA
    for i in range(n):
        for char in tape_symbols:
            delta.append((f"{chars_processed_in_current_block_counter}", char, f"{chars_processed_in_current_block_counter}", char, -1))

        # Add the transition once we have hit the left end marker
        delta.append((f"{chars_processed_in_current_block_counter}", ">", f"q{q_tracker}", ">", 1))

        # Add the "jump forward transitions" that are based on the chars_proccesed_in_current_block_counter until we are at the correct position
        for i in range(chars_processed_in_current_block_counter):
            delta.append((f"q{q_tracker}", "a'", f"q{q_tracker + 1}", "a'", 1))
            delta.append((f"q{q_tracker}", "b'", f"q{q_tracker + 1}", "b'", 1))  
            q_tracker += 1
        
        # Add the two transitions based on whether we say a' or b' from the correct position of the initial block
        delta.append((f"q{q_tracker}", "a'", f"a{chars_processed_in_current_block_counter + 1}", "a'", 1))
        delta.append((f"q{q_tracker}", "b'", f"b{chars_processed_in_current_block_counter + 1}", "b'", 1))

        # Add all the movement transitions that get us from the initial block back to the new element in the current block
        for char in tape_symbols:
            for value in [f"a{chars_processed_in_current_block_counter + 1}", f"b{chars_processed_in_current_block_counter + 1}"]:
                delta.append((value, char, value, char, 1))
        
        # Add the transitions based on whether the value in sigma is equal to the left most unprocessed value
        delta.append((f"a{chars_processed_in_current_block_counter + 1}", "a", f"{chars_processed_in_current_block_counter + 1}", "/", -1))
        delta.append((f"a{chars_processed_in_current_block_counter + 1}", "b", f"{chars_processed_in_current_block_counter + 1}", "X", -1))
        delta.append((f"b{chars_processed_in_current_block_counter + 1}", "a", f"{chars_processed_in_current_block_counter + 1}", "X", -1))
        delta.append((f"b{chars_processed_in_current_block_counter + 1}", "b", f"{chars_processed_in_current_block_counter + 1}", "/", -1))

        q_tracker += 1
        
        # Increment the chars proccessed so far variable
        chars_processed_in_current_block_counter += 1
    
    # Add the loop back to start transitions
    delta.append((f"{chars_processed_in_current_block_counter}", "/", "0", "/", -1))
    delta.append((f"{chars_processed_in_current_block_counter}", "X", "0", "X", -1))

    ### Add the final logic transitions

    # Add the two transitions that get you to final subgraph bit
    delta.append(("a1", "<", "qe", "<", -1))
    delta.append(("b1", "<", "qe", "<", -1))
    
    ##### EDIT THIS TO MAKE IT DYNAMIC AS IT WON'T ALWAYS BE JUST THIS NUMBER OF STATES WHEN N INCREASES ###
    # Add the transitions that essentially represent a string accepting the language 11
    # qr means q right, qw means q wrong
    

    for i in range(1, n):
        if i == 1:
            delta.append(("qe", "/", "qr", "/", -1))
            delta.append(("qe", "X", "qw", "X", -1))
            if i == n - 1:
                delta.append((f"q{'r' * i}", "X", "qe", "X", -1))
                delta.append((f"q{'r' * i}", "/", "qf", "/", -1))
                delta.append((f"q{'w' * i}", "/", "qe", "/", -1))
                delta.append((f"q{'w' * i}", "X", "qe", "X", -1))
        elif i == n - 1:
            # Last layer of the tree
            delta.append((f"q{'r' * (i - 1)}", "/", f"q{'r' * i}", "/", -1))
            delta.append((f"q{'r' * (i - 1)}", "X", f"q{'w' * i}", "X", -1))
            delta.append((f"q{'w' * (i - 1)}", "X", f"q{'w' * i}", "X", -1))
            delta.append((f"q{'w' * (i - 1)}", "/", f"q{'w' * i}", "/", -1))
            # Add the wrong transitions that loop back to qe
            delta.append((f"q{'r' * (i)}", "X", "qe", "X", -1))
            delta.append((f"q{'r' * (i)}", "/", "qf", "/", -1))
            delta.append((f"q{'w' * (i)}", "/", "qe", "/", -1))
            delta.append((f"q{'w' * (i)}", "X", "qe", "X", -1))
        else:
            # Add the transitions to current from previous
            delta.append((f"q{'r' * (i - 1)}", "/", f"q{'r' * i}", "/", -1))
            delta.append((f"q{'r' * (i - 1)}", "X", f"q{'w' * i}", "X", -1))
            delta.append((f"q{'w' * (i - 1)}", "/", f"q{'w' * i}", "/", -1))
            delta.append((f"q{'w' * (i - 1)}", "X", f"q{'w' * i}", "X", -1))

    # Add the final transitions that will allow you to move beyond the right end marker if a match was found
    delta.append(("qf", "/", "qf", "/", 1))
    delta.append(("qf", "X", "qf", "X", 1))
    delta.append(("qf", "<", "qf", "<", 1))

    # Extract the states required for the automaton
    states = {transition[0] for transition in delta} | {transition[2] for transition in delta}

    return (delta, states)

# This is correct, there are a 4 additional states created by the function however. This is because you can add some states that aren't necessary at a_n b_n as you technically won't see a' or b' when moving rightwards from here but can include them for the function readability


## For n = 2
print("Language where n = 2")
delta_2, states_2 = generate_delta(2)

automaton_2 = OneLimitedAutomata_rework(states=states_2, initial_state="q0", accepting_states=["qf"], sigma=["a", "b"], gamma=["X", "/", "a'", "b'"], delta=delta_2)

print(delta_2)

automaton_2.set_tape("aabbbbbaaa")
print(automaton_2.execute())

## For n = 3
# print("Language where n = 3")
delta_3, states_3 = generate_delta(3)

automaton_3 = OneLimitedAutomata_rework(states=states_3, initial_state="q0", accepting_states=["qf"], sigma=["a", "b"], gamma=["X", "/", "a'", "b'"], delta=delta_3)

# print(delta_3)

automaton_3.set_tape("babbbbaababbbbbaaaaab")
print(automaton_3.execute())

## For n = 4
print("Language where n = 4")
delta_4, states_4 = generate_delta(4)

automaton_4 = OneLimitedAutomata_rework(states=states_4, initial_state="q0", accepting_states=["qf"], sigma=["a", "b"], gamma=["X", "/", "a'", "b'"], delta=delta_4)

automaton_4.set_tape("ababbabaabab")
print(automaton_4.execute())





