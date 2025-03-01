def personal_sum(numbers):
    result_ = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result_ += num
        except TypeError:
            incorrect_data += 1
    return result_, incorrect_data

def calculate_average(numbers):
    try:
        sum = personal_sum(numbers)[0]
        k = len(numbers) - personal_sum(numbers)[1]
        return  sum / k
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
