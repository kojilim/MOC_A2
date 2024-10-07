from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

def q2a():
    return "0111"

def q2b(a, b):
    # Create new transitions for the NFA
    new_transitions = {}

    # Add transitions from DFA A to the NFA
    for state, trans in a.transitions.items():
        new_transitions[state] = {symbol: set(states) for symbol, states in trans.items()}  # Ensure states are sets

    # Add transitions from DFA B to the NFA
    for state, trans in b.transitions.items():
        if state in new_transitions:
            for symbol, states in trans.items():
                if symbol in new_transitions[state]:
                    new_transitions[state][symbol].update(states)
                else:
                    new_transitions[state][symbol] = set(states)
        else:
            new_transitions[state] = {symbol: set(states) for symbol, states in trans.items()}

    # Add epsilon transitions from DFA A's states to DFA B's start state
    for state in a.states:
        if state in new_transitions:
            if '' in new_transitions[state]:
                new_transitions[state][''].add(b.initial_state)
            else:
                new_transitions[state][''] = {b.initial_state}
        else:
            new_transitions[state] = {'': {b.initial_state}}

    # Add epsilon transitions from DFA B's accepting states back to DFA A's states
    for final_state in b.final_states:
        if final_state in new_transitions:
            if '' in new_transitions[final_state]:
                new_transitions[final_state][''].update(a.states)
            else:
                new_transitions[final_state][''] = set(a.states)
        else:
            new_transitions[final_state] = {'': set(a.states)}

    # Create the NFA with the new transitions
    nfa = NFA(
        states=a.states | b.states,  # Union of A and B's states
        input_symbols=a.input_symbols | b.input_symbols,  # Union of input symbols
        transitions=new_transitions,  # New transition table
        initial_state=a.initial_state,  # Start from DFA A's initial state
        final_states=a.final_states  # DFA A's accepting states
    )

    return nfa