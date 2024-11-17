# Unorderd Collection of Items
# Every Item is Unique
# Every element must be immutable (thats why can't contain list)
# A set is mutable
# Can be used for mathematical operations

my_set = {1, 2, 3, 4}
print(type(my_set))
my_set_1 = {1, 1, 1, 2, 3, 4, 5}
print(my_set_1)

#Set can't contain List because List is Mutable but We can create Set from List.
my_set_2 = set([1, 2, 2, 3, 3, 4])
print(my_set_2) #{1, 2, 3, 4}

my_set_3 = set()
print(type(my_set_3)) #empty set, empty dictionary - {}

my_set_4 = {1, 2, 3, 4}
my_set_4.add(5)
print(my_set_4) #{1, 2, 3, 4, 5}
my_set_4.update({3, 6, 7}, [8, 9])
print(my_set_4) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set_4.discard(3)
print(my_set_4) #{1, 2, 4, 5, 6, 7, 8, 9}
my_set_4.remove(8)
print(my_set_4) #{1, 2, 4, 5, 6, 7, 9}
# del deletes entire objet

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b)) #{1, 2, 3, 4, 5, 6, 7, 8} - a|b
print(a.intersection(b)) #{4, 5} - a&b
print(a.difference(b)) # {1, 2, 3} -> a-b
print(b.difference(a)) # {8, 6, 7} -> b-a
print(a.symmetric_difference(b)) # {1, 2, 3, 6, 7, 8} - a^b

# Set Functions - len, max, min, sorted, sum, in, not in

#frozenset
c = frozenset([1, 2, 3, 4, 5])
d = frozenset([4, 5, 6, 7, 8])
print(type(c | d)) #<class 'frozenset'>
print(type(c | b)) #<class 'frozenset'>
print(type(a | d)) #<class 'set'>