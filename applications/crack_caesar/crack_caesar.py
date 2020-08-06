# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

frequencyOrder = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D',
                  'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P',
                  'K', 'V', 'Q', 'J', 'X', 'Z']


with open('ciphertext.txt') as f:
    ipt = f.read()

frequencies = {}

for char in ipt:
    if char in frequencyOrder:
        if char not in frequencies.keys():
            frequencies[char] = 1
        else:
            frequencies[char] += 1

sorted_dict = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

pairs = {}

for i in range(len(sorted_dict)):
    pairs[sorted_dict[i][0]] = frequencyOrder[i]

decoded = ''

for char in ipt:
    if char in pairs.keys():
        decoded += pairs[char]
    else:
        decoded += char

print(decoded)
