from random import shuffle



def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot','carrots','potatoes']
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))

# print("The original words are : ",words)
# print("\n")
# print("The jumbled up words are : ",anagrams)

# print(list(map(jumble,words)))

print([ jumble(word) for word in words])
