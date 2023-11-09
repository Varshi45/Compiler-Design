class Grammar:
    def __init__(self):
        self.productions = {}

    def add_production(self, variable, rules):
        if variable not in self.productions:
            self.productions[variable] = []
        self.productions[variable].append(rules)

    def eliminate_left_factoring(self):
        new_productions = {}
        for variable, rules in self.productions.items():
            common_prefixes = self.find_common_prefixes(rules)
            if common_prefixes:
                new_variable = variable + "'"
                new_productions[variable] = [rule[len(common_prefixes):] + [new_variable] for rule in rules if rule[:len(common_prefixes)] == common_prefixes]
                new_productions[new_variable] = [[''] + rule[len(common_prefixes):] for rule in rules if rule[:len(common_prefixes)] == common_prefixes]
            else:
                new_productions[variable] = rules
        self.productions = new_productions

    def find_common_prefixes(self, rules):
        common_prefixes = []
        min_length = min(len(rule) for rule in rules)
        for i in range(min_length):
            prefix = rules[0][:i+1]
            if all(rule[:i+1] == prefix for rule in rules):
                common_prefixes.append(prefix)
            else:
                break
        return common_prefixes

    def display_productions(self):
        for variable, rules in self.productions.items():
            print(f"{variable} -> {' | '.join([' '.join(rule) for rule in rules])}")


my_grammar = Grammar()

my_grammar.add_production('A', [['a', 'b', 'c'], ['a', 'b', 'd'], ['e', 'f']])
my_grammar.add_production('B', [['a', 'b', 'g'], ['a', 'b', 'h'], ['i', 'j']])

print("Original Productions:")
my_grammar.display_productions()

my_grammar.eliminate_left_factoring()

print("\nProductions after Left-Factoring Elimination:")
my_grammar.display_productions()
