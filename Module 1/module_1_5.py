immutable_var = 'Murchik', 4 , True, 5.6, [30,18]
print(immutable_var)
# immutable_var [0] = 'Hvost' # Невозможно изменить элемент кортежа, ибо он неизменяемый тип данных (неизменяемая коллекция)
immutable_var[4][0] = 25 # Но возможно поменять изменяемый элемент, который хранится в коллекции
print(immutable_var)

mutable_list = ['Murchik', 4 , True, 5.6, [30,18]]
mutable_list[0] = 'Hvost'
print(mutable_list)

