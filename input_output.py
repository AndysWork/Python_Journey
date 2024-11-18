name = input('What is your name?')
print('Welcome {}.'.format(name))

def request_age():
    age=''
    while age.isdigit() == False:
        age = input('What is your age?')
        if age.isdigit() == False:
            print('Please enter digits only!!')
    return int(age)
request_age()

def play_again():
    answer = ''
    while answer.lower() not in ['y', 'n']:
        answer = input('Do you want to play again?')
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print('Enter Y or N Only!!!')
            
play_again()
        