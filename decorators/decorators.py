def greeting(x):
    print(x)
welcome = greeting
welcome('Andy')

def increase(x):
    return x + 1
def decrease(x):
    return x - 1
def operation(func, x):
    result = func(x)
    print(result)

operation(increase, 6)
operation(decrease, 3)

def i_am_being_called():
    def i_am_being_returned():
        print('Hi')
    return i_am_being_returned

new_test = i_am_being_called()
print(type(new_test)) #function
print(new_test())

#Closures
def base_multiply(base):
    def multiply_by(x):
        return base * x
    return multiply_by

multiply_by_6 = base_multiply(6)

print(multiply_by_6(10))

def original_func():
    print('I am the Original!')

def orch_func(func):
    def inner():
        print('I am from Inside!')
        func()
        print('I am from Outside!')
    return inner

my_test = orch_func(original_func)
print(my_test())

def divider_v2(func):
    def inner(a,b):
        print('Trying to divide ',a, 'by ',b)
        if b == 0:
            print('Can\'t divide by Zero!')
            return
        return func(a,b)
    return inner

@divider_v2 #decorator syntax
def divide(a,b):
    return a/b

print(divide(10,2))


def generic_decorator(func):
    def inner(*args, **kwargs):
        print('I can decorate any functions!')
        return func(*args, **kwargs)
    return inner
@generic_decorator #decorator syntax
def divider(a,b):
    return a/b

print(divider(10,2))