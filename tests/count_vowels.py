def count_vowels(text):
    vowels = "AEIOUaeiou"
    vowel_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1

    return vowel_count


text = "this is a test of counting syllables, a very simple test"
vowel_count = count_vowels(text)
print("Number of vowels:", vowel_count)
