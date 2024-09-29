my_dict = {'Vladislav': 1979, 'Vladimir': 1956, 'Anton': 1984}
print(my_dict)
print(my_dict['Vladislav'])
print(my_dict.get('Anna'))
my_dict.update ({'Sasha': 2006, 'Ira': 1958})
print(my_dict)
del my_dict ['Vladislav']
print(my_dict)
print(my_dict.get('Vladislav'))
print(my_dict.pop('Anton'))
print(my_dict)
#
my_set = {1,2,3,5,2,3,4,6,4,2,'Tru',43, 72.11,43}
print(my_set)
print(my_set.add(36))
print(my_set.add(44))
print(my_set)
print(my_set.discard('Tru'))
print(my_set)
