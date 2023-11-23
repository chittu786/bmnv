original_string = "Hello, World!"
word_count = 1
for char in original_string:
    if char.isspace():
        word_count += 1
print("Number of Words:", word_count)
