from OneLimitedAutomata_rework import OneLimitedAutomata_rework

# print("\u00E2")  # â
# print("b\u0302")  # b̂
# print("\u03A3")  # Σ (Capital Sigma)
# print("\u03B4")  # δ (Lowercase Delta)
# print("\u0393")  # Γ (Capital Gamma)
# print("\u2714")  # ✔
# print("\u2718")  # ✘
# print("\u2080")  # unicodefor0 → ₀
# print("\u2081")  # unicodefor1 → ₁
# print("\u2082")  # unicodefor2 → ₂
# print("\u2083")  # unicodefor3 → ₃
# print("\u2084")  # unicodefor4 → ₄
# print("\u2085")  # unicodefor5 → ₅
# print("\u2086")  # unicodefor6 → ₆
# print("\u2087")  # unicodefor7 → ₇
# print("\u2088")  # unicodefor8 → ₈
# print("\u2089")  # unicodefor9 → ₉
# print("\u2090")  # ₐ
# print("\u2091")  # ₑ
# print("\u2097")  # ₗ

unicode_numbers_dict = {0: "\u2080", 1: "\u2081", 2: "\u2082", 3: "\u2083", 4: "\u2084", 5: "\u2085", 6: "\u2086", 7: "\u2087", 8: "\u2088", 9: "\u2089"}

# Below is the definition of a 1LA that accepts the language of words from the paper where n = 2 and the number of repeats is greater than 0

automaton = OneLimitedAutomata_rework(states=["q₀", "0", "q₁", "a₁", "b₁", "1", "q₂", "q₃", "a₂", "b₂", "2", "qₑ", "q₄", "q₅", "qₗ"], initial_state="q₀", accepting_states=["qₗ"], Σ=["a", "b"], Γ=["✘", "✔", "â", "b̂"], δ=[("q₀", "a", "0", "â", 1), ("q₀", "b", "0", "b̂", 1), ("0", "a", "0", "â", -1), ("0", "b", "0", "b̂", -1), ("0", "â", "0", "â", -1), ("0", "b̂", "0", "b̂", -1), ("0", "✔", "0", "✔", -1), ("0", "✘", "0", "✘", -1), ("0", ">", "q₁", ">", 1), ("q₁", "â", "a₁", "â", 1), ("q₁", "b̂", "b₁", "b̂", 1), ("a₁", "✔", "a₁", "✔", 1), ("a₁", "✘", "a₁", "✘", 1), ("a₁", "â", "a₁", "â", 1), ("a₁", "b̂", "a₁", "b̂", 1), ("b₁", "✔", "b₁", "✔", 1), ("b₁", "✘", "b₁", "✘", 1), ("b₁", "â", "b₁", "â", 1), ("b₁", "b̂", "b₁", "b̂", 1), ("b₁", "a", "1", "✘", -1), ("b₁", "b", "1", "✔", -1), ("a₁", "a", "1", "✔", -1), ("a₁", "b", "1", "✘", -1), ("1", "â", "1", "â", -1), ("1", "b̂", "1", "b̂", -1), ("1", "✔", "1", "✔", -1), ("1", "✘", "1", "✘", -1), ("1", ">", "q₂", ">", 1), ("q₂", "â", "q₃", "â", 1), ("q₂", "b̂", "q₃", "b̂", 1), ("q₃", "â", "a₂", "â", 1), ("q₃", "b̂", "b₂", "b̂", 1), ("b₂", "✔", "b₂", "✔", 1), ("b₂", "✘", "b₂", "✘", 1), ("a₂", "✔", "a₂", "✔", 1), ("a₂", "✘", "a₂", "✘", 1), ("b₂", "a", "2", "✘", -1), ("b₂", "b", "2", "✔", -1), ("2", "✔", "0", "✔", -1), ("2", "✘", "0", "✘", -1), ("a₂", "a", "2", "✔", -1), ("a₂", "b", "2", "✘", -1), ("a₁", "<", "qₑ", "<",-1), ("b₁", "<", "qₑ", "<",-1), ("qₑ", "✘", "q₅", "✘", -1), ("qₑ", "✔", "q₄", "✔", -1), ("q₅", "✘", "qₑ", "✘", -1), ("q₅", "✔", "qₑ", "✔", -1), ("q₄", "✘", "qₑ", "✘", -1), ("q₄", "✔", "qₗ", "✔", 1), ("qₗ", "✔", "qₗ", "✔", 1), ("qₗ", "✘", "qₗ", "✘", 1), ("qₗ", "<", "qₗ", "<", 1)])

def update_digit_list(tracker_value, plus_one):
    if plus_one:
        return [int(digit) for digit in str(tracker_value + 1)]
    return [int(digit) for digit in str(tracker_value)]

# function that generates the transition function as well as all states required for the automaton
def generate_δ(n):
    δ = []
    tape_symbols = ["â", "b̂", "✔", "✘"]
    q_tracker = 0

    # Convert the number to a string and split it into individual digits
    q_tracker_digits = [int(digit) for digit in str(q_tracker)]
    q_tracker_digits_plus_one = [int(digit) for digit in str(q_tracker + 1)]


    ### Scanning and marking the initial block
    # Scanning the initial n-1 chars
    for i in range(n-1):
        digits = [int(digit) for digit in str(i)]
        digits_plus_one = [int(digit) for digit in str(i + 1)]
        if i == n-2:
            δ.append((f"q{"".join([unicode_numbers_dict[digit] for digit in digits])}", "a", "0", "â", 1))
            δ.append((f"q{"".join([unicode_numbers_dict[digit] for digit in digits])}", "b", "0", "b̂", 1))
        else:
            δ.append((f"q{"".join([unicode_numbers_dict[digit] for digit in digits])}", "a", f"q{"".join([unicode_numbers_dict[digit] for digit in digits_plus_one])}", "â", 1))
            δ.append((f"q{"".join([unicode_numbers_dict[digit] for digit in digits])}", "b", f"q{"".join([unicode_numbers_dict[digit] for digit in digits_plus_one])}", "b̂", 1))
        q_tracker += 1
        q_tracker_digits = update_digit_list(q_tracker, plus_one=False)
        q_tracker_digits_plus_one = update_digit_list(q_tracker, plus_one=True)
    
    # Add the nth char in the initial block
    δ.append(("0", "a", "0", "â", -1))
    δ.append(("0", "b", "0", "b̂", -1))

    ### Processing the nth char in the new block
    chars_processed_in_current_block_counter = 0
    # Convert the number to a string and split it into individual digits
    chars_processed_in_current_block_counter_digits = [int(digit) for digit in str(chars_processed_in_current_block_counter)]
    chars_processed_in_current_block_counter_digits_plus_one = [int(digit) for digit in str(chars_processed_in_current_block_counter + 1)]

    # We have n repetitions of the general pattern observed in the DFA
    for i in range(n):
        for char in tape_symbols:
            δ.append((f"{chars_processed_in_current_block_counter}", char, f"{chars_processed_in_current_block_counter}", char, -1))

        # Add the transition once we have hit the left end marker
        δ.append((f"{chars_processed_in_current_block_counter}", ">", f"q{"".join([unicode_numbers_dict[digit] for digit in q_tracker_digits])}", ">", 1))

        # Add the "jump forward transitions" that are based on the chars_proccesed_in_current_block_counter until we are at the correct position
        for i in range(chars_processed_in_current_block_counter):
            δ.append((f"q{"".join([unicode_numbers_dict[digit] for digit in q_tracker_digits])}", "â", f"q{"".join([unicode_numbers_dict[digit] for digit in q_tracker_digits_plus_one])}", "â", 1))
            δ.append((f"q{"".join([unicode_numbers_dict[digit] for digit in q_tracker_digits])}", "b̂", f"q{"".join([unicode_numbers_dict[digit] for digit in q_tracker_digits_plus_one])}", "b̂", 1))  
            q_tracker += 1
            q_tracker_digits = update_digit_list(q_tracker, plus_one=False)
            q_tracker_digits_plus_one = update_digit_list(q_tracker, plus_one=True)
        
        # Add the two transitions based on whether we say â or b̂ from the correct position of the initial block
        δ.append((f"q{"".join([unicode_numbers_dict[digit] for digit in q_tracker_digits])}", "â", f"a{"".join([unicode_numbers_dict[digit] for digit in chars_processed_in_current_block_counter_digits_plus_one])}", "â", 1))
        δ.append((f"q{"".join([unicode_numbers_dict[digit] for digit in q_tracker_digits])}", "b̂", f"b{"".join([unicode_numbers_dict[digit] for digit in chars_processed_in_current_block_counter_digits_plus_one])}", "b̂", 1))

        # Add all the movement transitions that get us from the initial block back to the new element in the current block
        for char in tape_symbols:
            for value in [f"a{"".join([unicode_numbers_dict[digit] for digit in chars_processed_in_current_block_counter_digits_plus_one])}", f"b{"".join([unicode_numbers_dict[digit] for digit in chars_processed_in_current_block_counter_digits_plus_one])}"]:
                δ.append((value, char, value, char, 1))
        
        # Add the transitions based on whether the value in Σ is equal to the left most unprocessed value
        δ.append((f"a{"".join([unicode_numbers_dict[digit] for digit in chars_processed_in_current_block_counter_digits_plus_one])}", "a", f"{(chars_processed_in_current_block_counter + 1)}", "✔", -1))
        δ.append((f"a{"".join([unicode_numbers_dict[digit] for digit in chars_processed_in_current_block_counter_digits_plus_one])}", "b", f"{(chars_processed_in_current_block_counter + 1)}", "✘", -1))
        δ.append((f"b{"".join([unicode_numbers_dict[digit] for digit in chars_processed_in_current_block_counter_digits_plus_one])}", "a", f"{(chars_processed_in_current_block_counter + 1)}", "✘", -1))
        δ.append((f"b{"".join([unicode_numbers_dict[digit] for digit in chars_processed_in_current_block_counter_digits_plus_one])}", "b", f"{(chars_processed_in_current_block_counter + 1)}", "✔", -1))

        q_tracker += 1
        q_tracker_digits = update_digit_list(q_tracker, plus_one=False)
        q_tracker_digits_plus_one = update_digit_list(q_tracker, plus_one=True)
        
        # Increment the chars proccessed so far variable
        chars_processed_in_current_block_counter += 1
        chars_processed_in_current_block_counter_digits = update_digit_list(q_tracker, plus_one=False)
        chars_processed_in_current_block_counter_digits_plus_one = update_digit_list(q_tracker, plus_one=True)
    
    # Add the loop back to start transitions
    δ.append((f"{chars_processed_in_current_block_counter}", "✔", "0", "✔", -1))
    δ.append((f"{chars_processed_in_current_block_counter}", "✘", "0", "✘", -1))

    ### Add the final logic transitions

    # Add the two transitions that get you to final subgraph bit
    δ.append(("a₁", "<", "qₑ", "<", -1))
    δ.append(("b₁", "<", "qₑ", "<", -1))

    for i in range(1, n):
        if i == 1:
            δ.append(("qₑ", "✔", "qᵣ", "✔", -1))
            δ.append(("qₑ", "✘", "qw", "✘", -1))
            if i == n - 1:
                δ.append((f"q{'ᵣ' * i}", "✘", "qₑ", "✘", -1))
                δ.append((f"q{'ᵣ' * i}", "✔", "qₗ", "✔", -1))
                δ.append((f"q{'ₓ' * i}", "✔", "qₑ", "✔", -1))
                δ.append((f"q{'ₓ' * i}", "✘", "qₑ", "✘", -1))
        elif i == n - 1:
            # Last layer of the tree
            δ.append((f"q{'ᵣ' * (i - 1)}", "✔", f"q{'ᵣ' * i}", "✔", -1))
            δ.append((f"q{'ᵣ' * (i - 1)}", "✘", f"q{'ₓ' * i}", "✘", -1))
            δ.append((f"q{'ₓ' * (i - 1)}", "✘", f"q{'ₓ' * i}", "✘", -1))
            δ.append((f"q{'ₓ' * (i - 1)}", "✔", f"q{'ₓ' * i}", "✔", -1))
            # Add the wrong transitions that loop back to qₑ
            δ.append((f"q{'ᵣ' * (i)}", "✘", "qₑ", "✘", -1))
            δ.append((f"q{'ᵣ' * (i)}", "✔", "qₗ", "✔", -1))
            δ.append((f"q{'ₓ' * (i)}", "✔", "qₑ", "✔", -1))
            δ.append((f"q{'ₓ' * (i)}", "✘", "qₑ", "✘", -1))
        else:
            # Add the transitions to current from previous
            δ.append((f"q{'ᵣ' * (i - 1)}", "✔", f"q{'ᵣ' * i}", "✔", -1))
            δ.append((f"q{'ᵣ' * (i - 1)}", "✘", f"q{'ₓ' * i}", "✘", -1))
            δ.append((f"q{'ₓ' * (i - 1)}", "✔", f"q{'ₓ' * i}", "✔", -1))
            δ.append((f"q{'ₓ' * (i - 1)}", "✘", f"q{'ₓ' * i}", "✘", -1))

    # Add the final transitions that will allow you to move beyond the right end marker if a match was found
    δ.append(("qₗ", "✔", "qₗ", "✔", 1))
    δ.append(("qₗ", "✘", "qₗ", "✘", 1))
    δ.append(("qₗ", "<", "qₗ", "<", 1))

    # Extract the states required for the automaton
    states = {transition[0] for transition in δ} | {transition[2] for transition in δ}

    return (δ, states)

## For n = 2
print("Language where n = 2")
δ_2, states_2 = generate_δ(2)

print(δ_2)

automaton_2 = OneLimitedAutomata_rework(states=states_2, initial_state="q₀", accepting_states=["qₗ"], Σ=["a", "b"], Γ=["✘", "✔", "â", "b̂"], δ=δ_2)

automaton_2.set_tape("aabbbbbaaa")
print(automaton_2.execute())

## For n = 3
print("Language where n = 3")
δ_3, states_3 = generate_δ(3)

automaton_3 = OneLimitedAutomata_rework(states=states_3, initial_state="q₀", accepting_states=["qₗ"], Σ=["a", "b"], Γ=["✘", "✔", "â", "b̂"], δ=δ_3)

print(δ_3)

automaton_3.set_tape("babbbbaababbbbbaaaaab")
print(automaton_3.execute())

## For n = 4
print("Language where n = 4")
δ_4, states_4 = generate_δ(4)

automaton_4 = OneLimitedAutomata_rework(states=states_4, initial_state="q₀", accepting_states=["qₗ"], Σ=["a", "b"], Γ=["✘", "✔", "â", "b̂"], δ=δ_4)

automaton_4.set_tape("ababbabaabab")
print(automaton_4.execute())





