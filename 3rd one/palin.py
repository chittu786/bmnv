original_string = "level"
is_palindrome = True
for i in range(len(original_string)//2):
    if original_string[i] != original_string[-i-1]:
        is_palindrome = False
        break
print("Is Palindrome:", is_palindrome)
