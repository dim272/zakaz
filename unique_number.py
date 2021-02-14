# Запрашиваем у пользователя несколько чисел
userInput = input("Введите не менее 3-х цифр разделяя их пробелом: ")
# Формируем из этого список
userList = list(map(str, userInput.split(' ')))


def search(list):
    i = 1
    lenList = len(list)

    while i <= lenList:
        # Берём элемент списка по индексу
        x = list[i-1]
        # Проверяем сколько совпадений в списке
        # Если сопадение 1, значит это искомое число
        if list.count(x) == 1:
            return x
        i += 1


result = search(userList)

if result is None:
    print('Все числа одинаковые')
else:
    print('Уникальное число:', result)
