import re


def histo(s):
    dictionary = {}
    s = re.sub(r"[^\w\d'\s]", '', s)
    for word in s.lower().split():
        if word not in dictionary.keys():
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    histogram = {}
    maxLength = 0
    for word in dictionary:
        if len(word) > maxLength:
            maxLength = len(word)
        key = dictionary[word]
        if key not in histogram.keys():
            histogram[key] = [word]
        else:
            histogram[key] += [word]
    lengths = list(histogram.keys())
    lengths = sorted(lengths, reverse=True)
    for length in lengths:
        printable = sorted(histogram[length])
        for word in printable:
            word = word + (' ' * (maxLength - len(word)) + '  ' + ('#' * length))
            print(word)


with open('robin.txt') as f:
    ipt = f.read()

histo(ipt)
