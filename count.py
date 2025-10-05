def count_vowels_consonents(s):
    """Count the number of vowels and consonants in a user-input string."""
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    print(f"Vowels: {v_count}, Consonants: {c_count}")
s = input("Enter a string: ")
count_vowels_consonents(s)