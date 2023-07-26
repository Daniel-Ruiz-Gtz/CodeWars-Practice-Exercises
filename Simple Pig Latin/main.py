"Simple Pig Latin"
"""
Instructions
Output
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    words = text.split()
    pig_latin_words = []

    for word in words:
        if word.isalpha():
            modified_word = word[1:] + word[0] + "ay"
        else:
            modified_word = word

        pig_latin_words.append(modified_word)

    new_sentence = " ".join(pig_latin_words)
    return new_sentence
    
print(pig_it("Good Morning Daniel !"))

"Quick Solution"

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

print(pig_it("Good Morning Daniel !"))