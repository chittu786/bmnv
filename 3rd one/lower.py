original_string = "Hello, World!"
lowercase_string = ""

for char in original_string:
    if 'A' <= char <= 'Z':
        lowercase_string += chr(ord(char) + 32)
    else:
        lowercase_string += char

print("Lowercase String:", lowercase_string)
