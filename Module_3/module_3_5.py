def get_multiplied_digits (number): #Вариант из задачи
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number)>1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

def get_multiplied_digits_2 (number): #Вариант с учётом 0
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number)>1:
        if str_number[1] == '0':
            return 0
        else:
            return first * get_multiplied_digits_2(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits_2(40203)
print(result)

