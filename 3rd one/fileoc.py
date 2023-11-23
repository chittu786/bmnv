original_string = "Hello, World!"
target_char = 'o'
char_count = 0
for char in original_string:
    if char == target_char:
        char_count += 1
print(f"Occurrences of '{target_char}':", char_count)
