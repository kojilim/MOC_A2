from automata.fa.nfa import NFA

def q2a():
    return "0111"

def q2b(a, b):
    # 'a' is the DFA for LA (even-length strings of 0s)
    # 'b' is the DFA for LB (even-length strings of 1s)
    
    # Combine the states of DFA A and DFA B
    combined_states = a.states.union(b.states)
    
    # Combine the input symbols
    combined_input_symbols = a.input_symbols.union(b.input_symbols)
    
    # Create the transition function for the NFA
    combined_transitions = {state: transitions.copy() for state, transitions in a.transitions.items()}
    for state in b.transitions:
        combined_transitions[state] = b.transitions[state].copy()

    # Add epsilon transitions from every state in DFA A to the start state of DFA B
    for state in a.states:
        if state not in combined_transitions:
            combined_transitions[state] = {}
        combined_transitions[state][''] = {b.initial_state}

    # Add epsilon transitions from the accepting state of DFA B back to every state in DFA A
    for state in a.states:
        if b.final_states:
            for b_accept_state in b.final_states:
                if b_accept_state not in combined_transitions:
                    combined_transitions[b_accept_state] = {}
                combined_transitions[b_accept_state][''] = {state}

    # Create the NFA with the combined states and transitions
    nfa = NFA(
        states=combined_states,
        input_symbols=combined_input_symbols,
        transitions=combined_transitions,
        initial_state=a.initial_state,
        final_states=a.final_states.union(b.final_states)  # Combine the final states of A and B
    )

    return nfa
