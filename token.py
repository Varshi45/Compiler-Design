import tokenize
from io import BytesIO

# Function to tokenize a Python source code
def tokenize_python_code(source_code):
    tokens = []
    source_code_bytes = source_code.encode('utf-8')
    
    try:
        for token in tokenize.tokenize(BytesIO(source_code_bytes).readline):
            token_type = tokenize.tok_name[token.type]
            token_value = token.string
            tokens.append((token_type, token_value))
    except tokenize.TokenError:
        print("Error: Unable to tokenize the input source code.")

    return tokens

# Example usage
if __name__ == '__main__':
    input_file_path = 'your_source_code.py'  # Replace with the path to your unformatted Python source code file

    with open(input_file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()
    
    tokens = tokenize_python_code(source_code)

    # Filter tokens to extract desired types
    keywords = [value for _, value in tokens if _ == 'NAME' and value in keyword.kwlist]
    operators = [value for _, value in tokens if _ == 'OP']
    constant_values = [value for _, value in tokens if _ == 'NUMBER']

    print("Keywords:", keywords)
    print("Operators:", operators)
    print("Constant Values:", constant_values)
