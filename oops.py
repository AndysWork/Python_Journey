class Dog:
    '''User defined class'''
    kingdom = 'Animal' #Class_Attributes
    def __init__(self, name, age, breed): #dunder methods - act as a decorator for a class
        self.name = name
        self.age = age
        self.breed = breed
    
    # def description(self):
    #     return '{} is {} years old'.format(self.name, self.age)
    
    def __str__(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)
        
        
my_dog = Dog('Lucy', 2, 'Shitzu')
print(my_dog.name)

my_dog.age = 3
print(my_dog.age)

#print(my_dog.description())

print(my_dog.speak('Yaakk!'))
class ParentDog:
    '''User defined class'''
    kingdom = 'Animal' #Class_Attributes
    def __init__(self, name, age): #dunder methods - act as a decorator for a class
        self.name = name
        self.age = age
    
    # def description(self):
    #     return '{} is {} years old'.format(self.name, self.age)
    
    def __str__(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return '{} says - {}'.format(self.name, sound)
    
class Shitzhu(ParentDog): #Inheritance
    def speak(self, sound='Shitzu Suff!'): # Method Modified
        #return '{} says {}'.format(self.name, sound)
        return super().speak(sound) # Accesing Parent Method
class Dobarman(Dog):
    pass

dolly = Shitzhu('Dolly', 5)

print(dolly)
print(isinstance(dolly, ParentDog))
print(dolly.speak())

#Special Methods

class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance =  balance
        print('__init__ Account created with Balance {}'.format(self.balance))
    def getbalance(self):
        return self.balance
    def __repr__(self):
        return '__repr__ Account ({}, {})'.format(self.name, self.balance)
    def __str__(self):
        return '__str__ Account Name - {} Balance - {}'.format(self.name, self.balance)
    def __int__(self):
        return int(self.balance)
    def __float__(self):
        return float(self.balance)
    def __lt__(self, obj):
        try:
            return self.balance < obj.getbalance()
        except Exception as e:
            print('Do you want to compare two bank account balance?')
            
andy_account = BankAccount('Andy', 3000)
print(andy_account)
print(andy_account.__repr__())
        
        