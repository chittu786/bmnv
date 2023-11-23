original_string = "Hello, World!"
uppercase_string = ""
for char in original_string:
    uppercase_string += chr(ord(char) - 32) if 'a' <= char <= 'z' else char
print("Uppercase String:", uppercase_string)
