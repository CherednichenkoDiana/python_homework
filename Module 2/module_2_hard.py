from random import randint

def get_result (n):
    result = ''
    for i in range (1,n):
        for j in range (i+1, n):
            if (n % (i + j)) == 0 :
                result += str(i)
                result += str(j)
    return result

n = randint(3,20)
# n = int(input('Введите число первого камня: '))
print(n,'-', str(get_result(n)))
