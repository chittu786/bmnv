import re

def tokenize(input_string):
    # Define regular expressions for different tokens
    regex_patterns = [
        (r'\bif\b', 'IF'),
        (r'\belse\b', 'ELSE'),
        (r'\bwhile\b', 'WHILE'),
        (r'\bint\b', 'INT'),
        (r'\bfloat\b', 'FLOAT'),
        (r'\b\d+\b', 'NUMBER'),  # Match integers
        (r'\b\w+\b', 'IDENTIFIER'),  # Match identifiers (words)
        (r'\s+', 'SPACE'),  # Match spaces
        (r'.', 'INVALID'),  # Match any other character as invalid
    ]

    tokens = []
    while input_string:
        for pattern, token_type in regex_patterns:
            match = re.match(pattern, input_string)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                input_string = input_string[len(value):].lstrip()
                break
    return tokens

# Example usage:
code = '''
if x > 5:
    print("Hello")
else:
    print("World")
'''

tokens = tokenize(code)
for token in tokens:
    print(f'Token: {token[0]}, Type: {token[1]}')

