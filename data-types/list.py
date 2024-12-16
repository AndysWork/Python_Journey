shopping_list = ['Apple', 'Banana', 'Watermelon']
numbers_list = [1, 2, 3, 4, 5]
list_all = ['Apple', 10, True, 0.13]
list_advanced = ['Banana', 10, True, 0.13, [1, 2, 3, 4]]
tic_tac_toe = [
    [[' '], [' '], [' ']],
    [[' '], [' '], [' ']],
    [[' '], [' '], [' ']]
]
empty_list = []

print(list_advanced[4]) # [1, 2, 3, 4]
print(list_advanced[4][1]) #2
print(list_advanced[-3])
print(list_advanced[-1][-2]) #Using negative Index - 3

fruit_list = ['Apple', 'Banana', 'Watermelon', 'Guava', 'Peach', 'Litchi', 'Melon', 'Berry', 'Kiwi', 'Pears']

print(fruit_list[0:5])
print(fruit_list[5:9])
print(fruit_list[:3])
print(fruit_list[3:])
print(fruit_list[-9:])
print(fruit_list[:-2]) #All but not 2nd last
print(fruit_list[::-1]) #Reverse List
print(fruit_list[::2]) #Every 2nd element

fruit_list.sort()
print(fruit_list)

fruit_list.sort(reverse = True) #Changes actual list
print(fruit_list)

sorted_fruit_list = sorted(fruit_list, reverse = True) #Doesn't change the actual list
print(sorted_fruit_list)

fruit_list[0:2] = ['Cream', 'Jam']
print(fruit_list)

dummy_list = [1, 2, 3, 4]
plus_list = [5, 6]
append_list = [7, 8]
extend_list = [9, 10]

dummy_list += plus_list
print(dummy_list)

dummy_list.append(append_list)
print(dummy_list)

dummy_list.extend(extend_list)
print(dummy_list)

dummy_list.insert(0, 0)
print(dummy_list)

lng_list = ['C', 'C++', 'C#', 'JAVA', 'JS']
lng_list.remove('C++') #Removes first occurence
print(lng_list)
print(lng_list.pop())
print(lng_list.pop(2)) #POP by Index

comp_list = ['Apple', 'OnePlus', 'Samsung', 'Motorola', 'Nokia', 'Vivo']

del comp_list[4]
print(comp_list)

del comp_list[1:3]
print(comp_list)

# del comp_list #Delete the entire list elements & Object
# comp_list.clear() #Delete the list elements

comp_list[:1] = []
print(comp_list)

my_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
print(len(my_list))

num_list = range(0, 101, 10) #range(start, stop, step)
print(list(num_list)) #[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

names = ['Andy', 'CoffinDancer', 'Castle', 'DareDevil', 'WhiteDevil']
age = [33, 32, 30, 28, 22]
names_ages = zip(names, age)
print(names_ages) #<zip object at 0x00000145D48BFEC0>
print(list(names_ages)) #[('Andy', 33), ('CoffinDancer', 32), ('Castle', 30), ('DareDevil', 28), ('WhiteDevil', 22)]

fav_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 3, 9]
print(fav_numbers.index(3,3)) #index(value, start, stop)
print(fav_numbers.index(3, 1, 8)) #2 (First Occurence of 3 at 2nd position)

fv_numbers = [1, 1, 2, 1, 3, 4, 1, 2]
print(fv_numbers.count(1)) # 1 Present 4 times

fav_players = ['CR7', 'M20', 'Z18', 'N10']

print('CR7' in fav_players) #True
print('M10' in fav_players) #False
print('R10' not in fav_players) #True

test_text = 'Gourab'
print(list(test_text))

test_list = 'Apple, Banana, Watermelon'
print(test_list.split(',')) #['Apple', ' Banana', ' Watermelon']

a, b, c = test_list.split(',')
print(a, b, c) #Apple  Banana  Watermelon
print(' and '.join(test_list.split(','))) #Apple and  Banana and  Watermelon