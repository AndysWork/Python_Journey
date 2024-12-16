my_tuple = (1, 'spain', 0.49)
print(type(my_tuple))

my_tuple1 = ('Data')
print((type(my_tuple1))) #String
my_tuple2 = ('Andy',) #Whether we have a value in the right side or not for tuple der will be a comma before finish
print((type(my_tuple2)))

num_tuple =[1, 2, 3, 4, 5, [6, 7, 8], (9, 10, 11)]
print(num_tuple[4]) #5 
print(num_tuple[6]) #(9, 10, 11)
print(num_tuple[6][1]) #10
print(num_tuple[-1][-1]) #11
print(num_tuple[0:3]) #[1, 2, 3]

num_tuple[5][2] = 69
num_tuple.append(80)
num_tuple[5].append(70)
print(num_tuple)

text_tuple = ('One', 'Two', 'Three')
print(text_tuple + ('Four', 'Five', 'Six'))
print(text_tuple * 2) #('One', 'Two', 'Three', 'One', 'Two', 'Three')

#Tuple can't be deleted

#Tuple Method - Count, Index
#Tuple Packing & Unpacking