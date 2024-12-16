def welcome():
    ''' This Function will welcome the user. ''' #docstring
    print('Hey! Welcome to Python Functions!')
    print(welcome.__doc__) #Print the docstring
    print([].__doc__) #Built-in Mutable Sequence
welcome()

def welcome_update():
    message = 'I am returning value.'
    return message
print(welcome_update().upper())

def welcome_greet(first, last):
    print('Hey, {} {}. Welcome to Python Learning.'.format(first, last))
welcome_greet('Andy', 'Paul') #-Keyword Argument
welcome_greet(first='Andy', last='Paul') #-Positional Argument 

def get_nums(*nums):
    total = 0
    print(type(nums)) # args - <class 'tuple'>
    for num in nums:
        total += num
    print('Total is {}'.format(total))
get_nums(1, 2, 3, 54)

def get_nums_dict(**nums):
    print(type(nums)) # kwargs - <class 'dict'>
    for key, value in nums.items():
        print('Key is {} & Value is {}'.format(key, value))
get_nums_dict(Name='Andy', Age=33, City='Bengaluru')

double = lambda x: x*2 #Lambda Function - Annonymus Function
print(double(10))        

multi = lambda a, b: a*b
print(multi(6, 9))

#filter(function, iterable)

even_logic = lambda num: num%2 == 0
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(even_logic, data)))

odd_nums = [1, 3, 5, 7, 11, 13, 17, 19]
print(list(map(lambda x: x*2, odd_nums)))

#LEGB Rule - Local Enclosing Global Built-in

def num():
    num = 10 #Local Scope to the Function Block
    return num

word = 'Global' #Global Scope
def space():
    #word = 'Enclosing'
    def another_space():
        #word = 'Local' #Enclosing Scope
        print('I came from ' +word)
    another_space()
space()

x=100
def check(x):
    #global - global keyword 
    print('X was actually {}'.format(x))
    x=200
    print('X changed to {} due to Local Scope'.format(x))
check(x)