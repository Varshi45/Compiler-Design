class Grammar:
    def __init__(self):
        self.productions = {}

    def add_production(self, variable, rules):
        if variable not in self.productions:
            self.productions[variable] = []
        self.productions[variable].extend(rules)

def compute_lr0_items(grammar):
    lr0_items = set()

    for variable, rules in grammar.productions.items():
        for rule in rules:
            for i in range(len(rule) + 1):
                lr0_item = (variable, tuple(rule[:i]), tuple(rule[i:]))
                lr0_items.add(lr0_item)

    return lr0_items

my_grammar = Grammar()

my_grammar.add_production('S', [['A', 'b'], ['a']])
my_grammar.add_production('A', [['c']])

lr0_items = compute_lr0_items(my_grammar)

print("LR(0) Items:")
for item in lr0_items:
    print(f"{item[0]} -> {' '.join(item[1])} . {' '.join(item[2])}")
