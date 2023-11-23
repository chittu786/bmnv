def count_vowels_consonants(file_path):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    with open(file_path, 'r') as file:
        content = file.read()

    num_vowels = sum(1 for char in content if char in vowels)
    num_consonants = sum(1 for char in content if char in consonants)

    return num_vowels, num_consonants

# Example usage:
file_path = 'your_file.txt'  # Replace with the path to your file
vowel_count, consonant_count = count_vowels_consonants(file_path)

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
