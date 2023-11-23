number_of_words = 0
number_of_lines = 0
number_of_characters = 0

with open("C:/simp/data.txt", 'r') as file:
    for l in file:
      number_of_words += len(l.split())
      number_of_lines += 1
      number_of_characters = len(l)

print("No of words: ", number_of_words)
print("No of lines: ", number_of_lines)
print("No of characters: ", number_of_characters)
