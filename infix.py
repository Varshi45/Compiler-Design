def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(token):
        return token in precedence

    def has_higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    def infix_to_postfix_internal(infix_tokens):
        output = []
        stack = []

        for token in infix_tokens:
            if token.isalnum():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif is_operator(token):
                while stack and has_higher_precedence(stack[-1], token):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output

    infix_tokens = expression.split()
    postfix_tokens = infix_to_postfix_internal(infix_tokens)
    return ' '.join(postfix_tokens)

def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(token):
        return token in precedence

    def has_higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    def infix_to_prefix_internal(infix_tokens):
        infix_tokens.reverse()
        stack = []
        output = []

        for token in infix_tokens:
            if token.isalnum():
                output.append(token)
            elif token == ')':
                stack.append(token)
            elif token == '(':
                while stack and stack[-1] != ')':
                    output.append(stack.pop())
                stack.pop()
            elif is_operator(token):
                while stack and has_higher_precedence(stack[-1], token):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        output.reverse()
        return output

    infix_tokens = expression.split()
    prefix_tokens = infix_to_prefix_internal(infix_tokens)
    return ' '.join(prefix_tokens)

def infix_to_three_address_code(expression):
    operators = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV', '^': 'POW'}

    def is_operator(token):
        return token in operators

    def get_temp_variable():
        global temp_variable_count
        temp_variable_count += 1
        return f'T{temp_variable_count}'

    def infix_to_three_address_code_internal(infix_tokens):
        stack = []
        output = []
        temp_var_stack = []

        for token in infix_tokens:
            if token.isalnum():
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif is_operator(token):
                while stack and stack[-1] != '(' and operators[token] < operators[stack[-1]]:
                    op = stack.pop()
                    if len(temp_var_stack) >= 2:
                        temp_var1 = temp_var_stack.pop()
                        temp_var2 = temp_var_stack.pop()
                        temp_result = get_temp_variable()
                        output.append(f'{temp_result} = {temp_var2} {op} {temp_var1}')
                        temp_var_stack.append(temp_result)
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output

    infix_tokens = expression.split()
    three_address_code = infix_to_three_address_code_internal(infix_tokens)
    return three_address_code


infix_expression = "a + b * (c - d)"
temp_variable_count = 0

postfix_expression = infix_to_postfix(infix_expression)
print("Postfix Expression:", postfix_expression)

prefix_expression = infix_to_prefix(infix_expression)
print("Prefix Expression:", prefix_expression)

temp_variable_count = 0
three_address_code = infix_to_three_address_code(infix_expression)
print("Three-Address Code:")
for code in three_address_code:
    print(code)
