#print(dir(locals()['__builtins__']))

def divider(x,y):
    return x/y

try:
    result = divider(2, '1')
except ZeroDivisionError:
    print('You can\'t divide by Zero')
except:
    print('Are you sure that, you are inputting numbers?')
else:
    print('Everything runs Smoothly!')
    print(result)
finally:
    print('Executed!!')


while True:
    try:
        data = int(input('Please enter a number'))
    except:
        print('This is not a number!')
        continue
    else:
        print('Good Choice')
        break
print(data)

# User-defined errors

# age = 'Thirty'
# if age is not int:
#     raise TypeError('Sorry! This is not an Integer')

def play_again():
    replay = input('Do you want to play again?')
    if replay.lower() not in ['yes', 'no']:
        raise ValueError('Value should be yes or no')
play_again()

class UserDefinedException(Exception):
    def __init__(self, message):
        self.message = message
try:
    marks = int(input('What\'s your marks?'))
    print('You have scored '+ str(marks) + ' marks!')
    if marks<36:
        raise UserDefinedException('You didn\'t get enough marks')
except UserDefinedException as err:
    print(err.message)
else:
    print('Congratulation\'s!! You Passed the Exam.')


class ScoreChecker(Exception):
    def __init__(self, score, message='You lost the game!'):
        self.score = score
        self.message = message
    def __str__(self):
        return 'You scored {}! {}'.format(self.score, self.message)

score = int(input('Enter your score '))
if score< 36:
    raise ScoreChecker(score)