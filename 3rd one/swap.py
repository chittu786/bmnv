original_string = "Hello, World!"
swapped_case_string = ""
for char in original_string:
    if 'a' <= char <= 'z':
        swapped_case_string += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        swapped_case_string += chr(ord(char) + 32)
    else:
        swapped_case_string += char
print("Swapped Case String:", swapped_case_string)
