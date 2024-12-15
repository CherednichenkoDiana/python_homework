def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        if num == 2:
            return 'Простое'
        for i in range(2,num):
            if num % i == 0:
                return 'Составное'
            if i == num-1:
                return 'Простое'
    return wrapper

@is_prime
def sum_three(*args):
    result = 0
    for num in args:
        result += int(num)
    return result


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
