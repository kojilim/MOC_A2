from automata.fa.dfa import DFA

def q1a():
    # Define the DFA states, input symbols, transitions, initial state, and accepting states
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
    input_symbols = {'0', '1'}
    
    # DFA transition function (correcting '0' to 'q0')
    transitions = {
        'q0': {'0': 'q1', '1': 'q0'},  # Start first block on '0'
        'q1': {'0': 'q2', '1': 'q0'},  # First block is odd-length, next '0' makes it even
        'q2': {'0': 'q1', '1': 'q3'},  # First block is even, move to q3 after '1'
        'q3': {'0': 'q4', '1': 'q3'},  # Start second block after one even-length block
        'q4': {'0': 'q5', '1': 'q3'},  # Second block is odd-length, next '0' makes it even
        'q5': {'0': 'q6', '1': 'q6'},  # Two even-length blocks detected, transition to q6 on '0' or '1'
        'q6': {'0': 'q6', '1': 'q6'}   # Accepting state: once here, accept everything
    }
    
    # Initial state is 'q0', final accepting states are 'q5' and 'q6'
    initial_state = 'q0'
    final_states = {'q5', 'q6'}

    # Create and return the DFA instance
    dfa = DFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )
    
    return dfa


def q1b():
    return "(0|1)*00(0|1)*00(0|1)*"