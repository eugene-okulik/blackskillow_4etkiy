number = 4

print("Угадайте цифру от 0 до 9")
user_number = int(input())
while number != user_number:
    print('попробуйте снова')
    user_number = int(input())
print('Поздравляю! Вы угадали!')
