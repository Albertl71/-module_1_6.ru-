my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Dict:", my_dict)
print("Existing value:", my_dict.get('Masha'))
print("Not existing value:", my_dict.get('Ivan'))
my_dict['Kamila'] = 1981
my_dict['Artem'] = 1985
deleted_value = my_dict.pop('Egor')
print("Deleted value:", deleted_value)
print("Modified dictionary:", my_dict)
my_set = {1, 'Яблоко', 42.314, 'Яблоко'}
print("Set:", my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print("Modified set:", my_set)