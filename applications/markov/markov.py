import random

dictionary = {}

# Read in all the words in one go
with open('./input.txt') as f:
    words = f.read().split()
    for i in range(len(words) - 1):
        if words[i] not in dictionary.keys():
            dictionary[words[i]] = [words[i + 1]]
        else:
            dictionary[words[i]] += [words[i + 1]]
    allWords = list(dictionary.keys())
    stopChars = ['.', '"', '?', '!']
    stopWords = [word for word in allWords if word[-1] in stopChars]
    startWords = [word for word in allWords if word[0] == word[0].upper() and word not in stopWords]
    for i in range(5):
        start = random.choice(startWords)
        sentence = start
        currentWord = start
        while currentWord not in stopWords:
            choices = dictionary[currentWord]
            currentWord = random.choice(choices)
            sentence += ' ' + currentWord
        print('---', sentence)
