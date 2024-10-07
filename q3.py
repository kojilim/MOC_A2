from automata.pda.npda import NPDA

def fill_in_epsilon_stack_moves(stack_alphabet, table):
    """Convert Sipser-style epsilon transitions to automata-lib format."""
    for f in table.values():
        for g in f.values():
            if '' not in g:
                continue
            for b in stack_alphabet:
                # Create new transitions that replace the top of the stack with itself
                new_transitions = {(q, (s, b)) for (q, s) in g['']}
                if b in g:
                    g[b] |= new_transitions
                else:
                    g[b] = new_transitions
            del g['']  # Remove the empty symbol once converted
    return table

def q3a():
    # Define the states, input symbols, and stack symbols
    states = {'q0', 'q1', 'q2', 'q3', 'q4'}
    input_symbols = {'a', 'b'}
    stack_symbols = {'a', '$'}

    # Define the transition table (before epsilon stack transformation)
    transitions = {
        'q0': {
            '': {  # Epsilon transition
                '$': {('q1', '$')}  # Push $ onto the stack
            }
        },
        'q1': {
            'a': {
                '$': {('q1', ('a', '$'))},  # Push 'a' onto the stack with $ at the bottom
                'a': {('q1', ('a', 'a'))},  # Push another 'a' onto the stack if 'a' is on top
            },
            '': {  # Epsilon transition to q2
                '$': {('q2', '$')},  # Move to q2 with $ on the stack
                'a': {('q2', 'a')}   # Move to q2 with 'a' still on the stack
            }
        },
        'q2': {
            'a': {
                'a': {('q2', '')}  # Pop 'a' from the stack on 'a' input
            },
            'b': {
                'a': {('q3', '')}  # Pop 'a' from the stack on 'b' input and move to q3
            }
        },
        'q3': {
            'a': {
                'a': {('q3', '')}  # Pop 'a' from the stack on 'a'
            },
            'b': {
                'a': {('q3', '')}  # Pop 'a' from the stack on 'b'
            },
            '': {  # Epsilon transition when stack has $
                '$': {('q4', '$')}  # Move to q4 (accept state) if stack has $
            }
        }
    }

    # Convert epsilon transitions using the fill_in_epsilon_stack_moves function
    transitions = fill_in_epsilon_stack_moves(stack_symbols, transitions)

    # Define the NPDA
    npda = NPDA(
        states=states,
        input_symbols=input_symbols,
        stack_symbols=stack_symbols,
        transitions=transitions,
        initial_state='q0',
        initial_stack_symbol='$',
        final_states={'q4'},
        acceptance_mode='both'  # Accept by both final state and empty stack
    )

    return npda