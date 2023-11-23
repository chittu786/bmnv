original_string = " Hello,  World! "
trimmed_string = ""
for char in original_string:
    if char != ' ':
        trimmed_string += char
print("Trimmed String:", trimmed_string)
