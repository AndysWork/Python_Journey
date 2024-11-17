for item in range(1,100):
    if item%3==0 and item%5==0:
        print('FizzBuzz')
    elif item%3==0:
        print('Fizz')
    elif item%5==0:
        print('Buzz')
    else:
        print(item)

item =1 
while item in range(1,100):
    if item%3==0 and item%5==0:
        print('FizzBuzz')
    elif item%3==0:
        print('Fizz')
    elif item%5==0:
        print('Buzz')
    else:
        print(item)
    item += 1
    
a = 1
b = 1
while a<=3:
    print('Outer Loop number {}'.format(a))
    while b<=5:
        c = a*b
        print('Inner loop {} calculates {}*{}={}'.format(b, a, b, c))
        b += 1
    a += 1
    b = 1
    print('-----')
    
# break, continue, pass(for skipping loop action)

for i in [1, 2, 3, 4, 5]:
    print(i)
else:
    print('No more numbers in the list!')

alphabet = 'abcdefg'
my_dict = {}

for item in enumerate(alphabet): #enumerate returns iterable tuple
    my_dict[item[0]]=item[1]
print(my_dict)     

#List Comprehension
for i in range(0,20):
    if i % 2 == 0:
        print(i)
        
evens_for =[]
for x in range(11):
    evens_for.append(x*2)
print(evens_for)

evens_list = [(x*2) for x in range(11)]
print(evens_list)

evens_divisible = [(x*2) for x in range(11) if x*2 % 6 != 0]
print(evens_divisible)

#Dictionary Comprehension
my_test_dict = {}
for x in range(6):
    my_test_dict[x] = x*x
print(my_test_dict)

squares = {x: x*x for x in range(6)}
print(squares)

even_squares = {x: x*x for x in range(6) if x%2 == 0}
print(even_squares)

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# new_set = set() #1
new_set = {x*x for x in my_set} #2

# for x in my_set: #1
#     new_set.add(x*x) #1
print('My_Set Contains {}'.format(my_set))
print('New_Set Contains {}'.format(new_set))