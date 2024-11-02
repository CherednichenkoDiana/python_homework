def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding= 'utf-8')
    strings_positions = dict()
    i = 1
    for str in strings:
        tup = (i, file.tell())
        strings_positions[tup] = str
        str += '\n'
        file.write(str)
        i += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)