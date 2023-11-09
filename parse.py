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

def create_parsing_table(grammar, start_symbol):
    parsing_table = {}

    # Initialize sets
    first_sets = {}
    follow_sets = {}

    # Compute First Sets
    for variable in grammar.productions:
        compute_first_set(grammar, variable, first_sets)

    # Compute Follow Sets
    compute_follow_set(grammar, start_symbol, first_sets, follow_sets)

    # Fill in the parsing table
    for variable, rules in grammar.productions.items():
        for rule in rules:
            first_alpha = compute_first_set(grammar, rule[0], first_sets)
            for terminal in first_alpha:
                if terminal != '':
                    parsing_table[(variable, terminal)] = rule

            if '' in first_alpha:
                follow_A = compute_follow_set(grammar, variable, first_sets, follow_sets)
                for terminal in follow_A:
                    parsing_table[(variable, terminal)] = rule

    return parsing_table

my_grammar = Grammar()

my_grammar.add_production('S', [['A', 'B'], ['C']])
my_grammar.add_production('A', [['a', 'A'], []])
my_grammar.add_production('B', [['b', 'B'], []])
my_grammar.add_production('C', [['c', 'S', 'C'], []])

start_symbol = 'S'

parsing_table = create_parsing_table(my_grammar, start_symbol)

print("Predictive Parsing Table:")
for key, value in parsing_table.items():
    print(f"{key}: {value}")
