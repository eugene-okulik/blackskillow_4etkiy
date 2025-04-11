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


# Третий вариант через функцию.
def summa(resultat):
    print(int(resultat.split()[-1]) + 10, end=' ')


print()
summa(res1)
summa(res2)
summa(res3)
summa(res4)


# четвертый вариант через функцию и цикл(меньше строк).
def summa(resultat):
    for i in range(0, len(resultat)):
        print(int(str(resultat[i]).split()[-1]) + 10, end=' ')


print()
my_tuple = [res1, res2, res3, res4]
summa(my_tuple)
