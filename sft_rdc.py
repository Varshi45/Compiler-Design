class Grammar:
    def __init__(self):
        self.productions = {}

    def add_production(self, variable, rules):
        if variable not in self.productions:
            self.productions[variable] = []
        self.productions[variable].extend(rules)

def shift_reduce_parser(grammar, input_string):
    stack = ['$']
    input_buffer = list(input_string) + ['$']

    while True:
        print("Stack:", stack)
        print("Input Buffer:", ''.join(input_buffer))

        if stack[-1] in grammar.productions and input_buffer[0] in grammar.productions:
            # Try reducing
            for rule in grammar.productions[stack[-1]]:
                if rule == input_buffer[:len(rule)]:
                    stack = stack[:-len(rule)]  
                    stack.append(stack[-1])  
                    print("Reduce by:", ''.join(rule))
                    break
            else:
                print("Error: Cannot reduce")
                break
        else:
            # Shift
            stack.append(input_buffer.pop(0))
            print("Shift")

        if stack[-1] == '$' and len(input_buffer) == 1:
            print("Accept: String is in the language")
            break

my_grammar = Grammar()

my_grammar.add_production('S', [['a', 'A', 'b'], ['b', 'B', 'a']])
my_grammar.add_production('A', [['c'], []])
my_grammar.add_production('B', [['d'], []])

input_string = 'acbd'
shift_reduce_parser(my_grammar, input_string)
