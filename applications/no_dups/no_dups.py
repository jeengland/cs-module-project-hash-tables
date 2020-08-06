def no_dups(s):
    words = {}
    output = []
    s = s.split()
    for word in s:
        if word not in words.keys():
            output.append(word)
            words[word] = 1
    return ' '.join(output)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
