#Get sentence from user
sentence = input('Enter the sentence you want to translate : ').strip().lower()

#Spliting sentence into words
words = sentence.split()

#Converting words to pig latin
latin_words = []

for word in words :
    if word[0] in "aeiou" :
        latin_word = word + 'yay'
        latin_words.append(latin_word)

    else:
        vowel_pos = 0
        for letter in word :
            if letter not in "aeiou" :
                vowel_pos = vowel_pos +1
            else:
                break

        cons = word[:vowel_pos]
        rest = word[vowel_pos:]

        latin_word = rest + cons + 'ay'
        latin_words.append(latin_word)

#Stick back words back together
output = " ".join(latin_words)

#Printing final output
print(output)
