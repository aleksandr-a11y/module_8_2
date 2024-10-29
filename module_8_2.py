def personal_sum(*numbers):
    incorrect_data = 0
    result = 0
    for num in numbers:
        for i in num:
            try:
                result += i
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
                incorrect_data += 1
    return result, incorrect_data


def calculate_average(*numbers):
    if isinstance(*numbers, int):
        return None
    try:
        sum_ = personal_sum(*numbers)
        if len(*numbers) == 0:
            return 0
        else:
            return  sum_[0]/ (len(*numbers) -  sum_[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать