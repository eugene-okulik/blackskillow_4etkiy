words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
value = list(words.values())
key = list(words.keys())

for i in range(0, len(value)):
    for j in range(0, int(value[i])):
        print(key[i], end='')
    print('')
