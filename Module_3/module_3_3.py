def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)



print_params()
print_params([1,2],True)
print_params([1,2],c='hi')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Book', 1500, [20,True]]
values_dict = {'a':False, 'b':'Devil', 'c':56.5}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [[1,2],False]
print_params(*values_list_2,42)