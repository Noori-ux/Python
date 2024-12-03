sentence=input("enter a sentence: ")
def numberOfvowels(sentence):
    vowel_counter=0
    vowels="aeiou"
    for l in sentence:
        if l in vowels:
            vowel_counter+=1

    return vowel_counter

number_vowels=numberOfvowels(sentence)
print(f"Total number of vowels in {sentence} are {number_vowels}")
    
