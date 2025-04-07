text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')

print('Оригинал:', text)
words = text.split()
fin_text = []
for word in words:
    if word.endswith(','):
        word = word.replace(',', 'ing,')
        fin_text.append(word)
    elif word.endswith('.'):
        word = word.replace('.', 'ing.')
        fin_text.append(word)
    else:
        word = word + 'ing'
        fin_text.append(word)
print('Ремейк:', ' '.join(fin_text))
