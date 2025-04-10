res1 = 'результат операции: 42'
res2 = 'результат операции: 54'
res3 = 'результат работы программы: 209'
res4 = 'результат: 2'

# Перый варинат, 1 строка.
print(int(res1.split()[-1]) + 10, int(res2.split()[-1]) + 10, int(res3.split()[-1]) + 10, int(res4.split()[-1]) + 10)

# Второй вариант больше строк, без повторов.
my_tuple = [res1, res2, res3, res4]
for i in range(0, len(my_tuple)):
    print(int(str(my_tuple[i]).split()[-1]) + 10, end=' ')
