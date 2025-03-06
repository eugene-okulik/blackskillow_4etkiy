text1 = 'результат операции: 42'
stop1 = text1.index(":") + 2
print(stop1)
number1 = int(text1[(stop1):])
print(number1 + 10)

text2 = 'результат операции: 514'
stop2 = text2.index(":") + 2
print(stop2)
number2 = int(text2[(stop2):])
print(number2 + 10)

text3 = 'результат работы программы: 9'
stop3 = text3.index(":") + 2
print(stop3)
number3 = int(text3[(stop3):])
print(number3 + 10)
