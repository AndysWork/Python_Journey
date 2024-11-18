import random
def guess_the_number():
    count = 5
    number = random.randint(1, 30)
    while count != 0:
        answer = input('Please Enter Your Guess')
        if int(answer) > number:
            print('Guess is Too High! {} tries remaining!'.format(count-1))
        elif int(answer) < number:
            print('Guess is Too Low! {} tries remaining!'.format(count-1))
        elif int(answer) == number:
            print('Winner! Correct Guess..')
            break
        count -= 1
    return count
if guess_the_number() == 0:
    print('Game Over!!')
    choice = input('Do you want to play again?')
    if choice.lower() == 'y':
        guess_the_number()
    elif choice.lower() == 'n':
        print('See You, Next Time..')