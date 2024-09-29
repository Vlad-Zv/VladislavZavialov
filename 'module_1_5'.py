immutable_var = (["Изменяемые" , 'объекты'], 1,2,[3], [4], True)
immutable_var_ = (["Изменяемые" , 'объекты'], ((1,2)*3),[3], [4], True)
immutable_var_1 = (["Изменяемые" , 'объекты'], [1,2,[3], [4]], True)
list_ = [["Изменяемые" , 'объекты'], 1,2,[3], [4], True]
print(immutable_var)
print(immutable_var_)
print(immutable_var_1)
print(immutable_var[0])
print(immutable_var.__sizeof__())
print(list_.__sizeof__())
mutable_list = [1,2,'a','b']
print(mutable_list)
mutable_list.extend (['Modified'])
print(mutable_list)
