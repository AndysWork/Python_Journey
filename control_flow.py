it_is_cold = True

if it_is_cold:
    print('Winter is Coming!')
    

if 1>0:
    print('Yes! It is..')
    print('Correct!')
print('Finished!')

age = 21

if age<18:
    print('Not old enough.. :-(')
else:
    print('Enjoy! Watch the movie.')
    
score = 89
if score >= 80:
    print('GOLD!')
elif score >= 60:
    print('Silver!')
elif score >= 40:
    print('Bronze!')

shopping_list = []
item = 'Apples'

if item not in shopping_list:
    shopping_list.append(item)
print(shopping_list)