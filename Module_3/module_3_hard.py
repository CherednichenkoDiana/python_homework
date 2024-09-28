
def calculate_structure_sum(*structure):
    sum_ = 0
    for data in structure:
        if isinstance(data, list) or isinstance(data, set) or isinstance(data, tuple):
            for data_2 in data:
                sum_ += calculate_structure_sum(data_2)
            return sum_
        elif isinstance(data,int) or isinstance(data, bool):
            return int(data)
        elif isinstance(data, float):
            return float(data)
        elif isinstance(data,str):
            return len(data)
        elif isinstance(data,dict):
            for key, value in data.items():
                sum_ += calculate_structure_sum(key)
                sum_ += calculate_structure_sum(value)
            return sum_
        else:
            return sum_

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}], False, 0.9)
]

result = calculate_structure_sum(data_structure)
print(result)