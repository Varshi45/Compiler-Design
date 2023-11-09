class Grammar:
    def __init__(self):
        self.productions = {}

    def add_production(self, variable, rules):
        if variable not in self.productions:
            self.productions[variable] = []
        self.productions[variable].append(rules)

    def eliminate_left_recursion(self):
        new_productions = {}
        for variable, rules in self.productions.items():
            alpha, beta = self.split_rules(variable, rules)
            if alpha:
                new_variable = variable + "'"
                new_productions[variable] = [rule + [new_variable] for rule in beta]
                new_productions[new_variable] = [[''] + [rule + [new_variable] for rule in alpha]]
            else:
                new_productions[variable] = rules
        self.productions = new_productions

    def split_rules(self, variable, rules):
        alpha = []
        beta = []
        for rule in rules:
            if rule and rule[0] == variable:
                alpha.append(rule[1:])
            else:
                beta.append(rule)
        return alpha, beta

    def display_productions(self):
        for variable, rules in self.productions.items():
            print(f"{variable} -> {' | '.join([' '.join(rule) for rule in rules])}")


my_grammar = Grammar()

my_grammar.add_production('A', [['A', 'a'], ['B']])
my_grammar.add_production('B', [['B', 'b'], ['A']])

print("Original Productions:")
my_grammar.display_productions()

my_grammar.eliminate_left_recursion()

print("\nProductions after Left Recursion Elimination:")
my_grammar.display_productions()
