class State:
    def __init__(self, label):
        self.label = label
        self.transitions = {}

class NFA:
    def __init__(self):
        self.states = []
        self.start_state = None
        self.accept_state = None

    def add_state(self, label):
        state = State(label)
        self.states.append(state)
        return state

    def add_transition(self, from_state, to_state, symbol):
        from_state.transitions[symbol] = to_state

def regex_to_nfa(regex):
    nfa = NFA()
    stack = []

    for char in regex:
        if char.isalpha() or char.isdigit():
            start_state = nfa.add_state(char)
            accept_state = nfa.add_state(None)
            nfa.add_transition(start_state, accept_state, char)
            stack.append((start_state, accept_state))
        elif char == '|':
            nfa_union(nfa, stack)
        elif char == '.':
            nfa_concatenate(nfa, stack)
        elif char == '*':
            nfa_closure(nfa, stack)

    if stack:
        (start_state, accept_state) = stack.pop()
        nfa.start_state = start_state
        nfa.accept_state = accept_state

    return nfa

def nfa_union(nfa, stack):
    accept_state = nfa.add_state(None)
    start_state = nfa.add_state(None)
    nfa.add_transition(start_state, accept_state, None)

    if stack:
        (s_start, s_accept) = stack.pop()
        nfa.add_transition(start_state, s_start, None)
        nfa.add_transition(s_accept, accept_state, None)

    stack.append((start_state, accept_state))

def nfa_concatenate(nfa, stack):
    if len(stack) >= 2:
        (s1_start, s1_accept) = stack.pop()
        (s2_start, s2_accept) = stack.pop()
        nfa.add_transition(s2_accept, s1_start, None)
        stack.append((s2_start, s1_accept))

def nfa_closure(nfa, stack):
    if stack:
        (s_start, s_accept) = stack.pop()
        accept_state = nfa.add_state(None)
        start_state = nfa.add_state(None)
        nfa.add_transition(start_state, accept_state, None)
        nfa.add_transition(start_state, s_start, None)
        nfa.add_transition(s_accept, accept_state, None)
        nfa.add_transition(s_accept, s_start, None)
        stack.append((start_state, accept_state))

regex = "a.b|c*"
nfa = regex_to_nfa(regex)

for state in nfa.states:
    print(f"State {state.label}:")
    for symbol, next_state in state.transitions.items():
        print(f"  --({symbol})--> State {next_state.label}")

print("Start state:", nfa.start_state.label)
print("Accept state:", nfa.accept_state.label)
