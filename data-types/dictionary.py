my_dict = {}
print(my_dict)

names = ['Andy', 'CoffinDancer', 'Castle', 'DareDevil', 'WhiteDevil']
age = [33, 32, 30, 28, 22]
my_dict = dict(zip(names, age))
print(my_dict)

print(my_dict['Andy'])
print(my_dict.get('Castle'))

shop_dict = {'Sugar' : 0.25, 'Maida': 0.45, 'Oil' : 0.89}
shop_dict['Oil'] = 1.45
shop_dict['Vegetables'] = 3.2
print(shop_dict)

print(shop_dict.pop('Butter', 1.2))
print(shop_dict.popitem())

del shop_dict['Maida']
print(shop_dict)

#del shop_dict OR shop_dict.clear()

print(shop_dict.items()) #dict_items([('Sugar', 0.25), ('Oil', 1.45)])
print(type(shop_dict.items())) #<class 'dict_items'>

print(shop_dict.keys()) #dict_keys(['Sugar', 'Oil'])
print(type(shop_dict.keys())) #<class 'dict_keys'>

print(shop_dict.values()) #dict_values([0.25, 1.45])
print(type(shop_dict.values())) #<class 'dict_values'>

print('Sugar' in shop_dict) #True
print('Bread' in shop_dict) #False
print(len(shop_dict))
print(sorted(shop_dict))
print(all(shop_dict))
print(bool('Sugar'))
print(any(my_dict))
