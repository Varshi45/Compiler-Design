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
            alpha, beta = self.split_rules(rules)
            if alpha:
                new_variable = variable + "'"
                new_productions[new_variable] = [rule + [new_variable] for rule in alpha] + [[]]
                new_productions[variable] = [rule + [new_variable] for rule in beta]
            else:
                new_productions[variable] = rules
        self.productions = new_productions

    def split_rules(self, rules):
        alpha = []
        beta = []
        for rule in rules:
            if rule and rule[0] == rule[-1]:
                alpha.append(rule[1:])
            else:
                beta.append(rule)
        return alpha, beta

    def find_first_sets(self):
        first_sets = {}
        for variable in self.productions:
            first_sets[variable] = set()

        for variable in self.productions:
            self.find_first(variable, first_sets)

        return first_sets

    def find_first(self, variable, first_sets):
        if variable in first_sets:
            return

        first_set = set()

        for rule in self.productions[variable]:
            if not rule:
                first_set.add('')
            elif rule[0] not in self.productions:
                first_set.add(rule[0])
            else:
                self.find_first(rule[0], first_sets)
                first_set.update(first_sets[rule[0]])

        first_sets[variable] = first_set

    def find_follow_sets(self, start_symbol):
        follow_sets = {variable: set() for variable in self.productions}
        follow_sets[start_symbol].add('$')

        for variable in self.productions:
            self.find_follow(variable, follow_sets, start_symbol)

        return follow_sets

    def find_follow(self, variable, follow_sets, start_symbol):
        for symbol in self.productions:
            for rule in self.productions[symbol]:
                if variable in rule:
                    idx = rule.index(variable)

                    for next_symbol in rule[idx + 1:]:
                        if next_symbol in self.productions:
                            follow_sets[variable].update(self.find_first(next_symbol))
                            if '' not in self.find_first(next_symbol):
                                break
                        else:
                            follow_sets[variable].add(next_symbol)

                    if '' in self.find_first(next_symbol):
                        follow_sets[variable].update(follow_sets[symbol])

    def display_productions(self):
        for variable, rules in self.productions.items():
            print(f"{variable} -> {' | '.join([' '.join(rule) for rule in rules])}")


my_grammar = Grammar()

my_grammar.add_production('S', [['A', 'B'], ['C']])
my_grammar.add_production('A', [['a', 'A'], []])
my_grammar.add_production('B', [['b', 'B'], []])
my_grammar.add_production('C', [['c', 'S', 'C'], []])

print("Original Productions:")
