from automata.fa.dfa import DFA

def q1a():
    # Define the DFA states, input symbols, transitions, initial state, and accepting state
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
    input_symbols = {'0', '1'}
    
    # DFA transition function to track blocks of 0's and handle even/odd blocks
    transitions = {
        'q0': {'0': 'q1', '1': 'q0'},  # No blocks seen yet, encountering '0' starts a block
        'q1': {'0': 'q2', '1': 'q0'},  # Odd-length block, next '0' turns it into even-length
        'q2': {'0': 'q1', '1': 'q3'},  # Even-length block completed, move to q3 on '1'
        'q3': {'0': 'q4', '1': 'q3'},  # Processing blocks, move to q4 if another block starts
        'q4': {'0': 'q5', '1': 'q3'},  # A second even-length block ends
        'q5': {'0': 'q4', '1': 'q5'}   # Accepting state: two even-length blocks found
    }

    # Initial state is 'q0'
    initial_state = 'q0'
    
    # Accepting state is 'q5' (when two even-length blocks of 0s have been seen)
    final_states = {'q5'}
    
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
    # Return the regular expression matching binary strings with at least two even-length blocks of 0's
    return "1*(00)1*(00)1*"