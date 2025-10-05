def count_vowel_consonant(s):
    v_count=c_count=0
    vowels = 'aeiouAEIOU'
    for ch in s:
        if ch.isalpha():
            if ch.lower() in vowels:
                v_count+=1
            else:
                c_count+=1
    return v_count, c_count
# Example usage:
s = input("Enter a string: ")
vowels, consonants = count_vowel_consonant(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")