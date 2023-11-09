class Grammar:
    def __init__(self):
        self.productions = {}

    def add_production(self, variable, rules):
        if variable not in self.productions:
            self.productions[variable] = []
        self.productions[variable].extend(rules)

def compute_first_set(grammar, variable, first_sets):
    if variable in first_sets:
        return first_sets[variable]

    first_set = set()
    for rule in grammar.productions.get(variable, []):
        if rule[0] == variable:
            continue  # Avoid left recursion
        first_set |= compute_first_set(grammar, rule[0], first_sets)
    first_sets[variable] = first_set
    return first_set

def compute_follow_set(grammar, variable, first_sets, follow_sets):
    if variable in follow_sets:
        return follow_sets[variable]

    follow_set = set()
    for v, rules in grammar.productions.items():
        for rule in rules:
            if variable in rule:
                idx = rule.index(variable)
                if idx < len(rule) - 1:
                    follow_set |= compute_first_set(grammar, rule[idx + 1], first_sets)
                if idx == len(rule) - 1 or ('' in compute_first_set(grammar, rule[idx + 1], first_sets)):
                    follow_set |= compute_follow_set(grammar, v, first_sets, follow_sets)

    follow_sets[variable] = follow_set
    return follow_set

# Example usage:

# Create a Grammar instance
my_grammar = Grammar()

# Add productions to the grammar
my_grammar.add_production('S', [['A', 'B'], ['C']])
my_grammar.add_production('A', [['a', 'A'], []])
my_grammar.add_production('B', [['b', 'B'], []])
my_grammar.add_production('C', [['c', 'S', 'C'], []])

first_sets = {}
follow_sets = {}

for variable in my_grammar.productions:
    compute_first_set(my_grammar, variable, first_sets)

compute_follow_set(my_grammar, 'S', first_sets, follow_sets)

print("First Sets:")
for variable, first_set in first_sets.items():
    print(f"First({variable}) = {first_set}")

print("\nFollow Sets:")
for variable, follow_set in follow_sets.items():
    print(f"Follow({variable}) = {follow_set}")
