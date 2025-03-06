# с помощью среза
text1 = 'результат операции: 42'
list_from_text1 = text1.split()
print(list_from_text1)
number1 = int(list_from_text1[-1:][0])
print(number1 + 10)

# с помощью index
text2 = 'результат операции: 514'
list_from_text2 = text2.split()
print(list_from_text2)
number2 = int(list_from_text2[list_from_text2.index('514')])
print(number2 + 10)

# с помощью среза и index
text3 = 'результат работы программы: 9'
list_from_text3 = text3.split()
print(list_from_text3)
srez = list_from_text3[-1:]
for_index3 = srez[0]
print(srez, for_index3)
number3 = int(list_from_text3[list_from_text3.index(for_index3)])
print(number3 + 10)
