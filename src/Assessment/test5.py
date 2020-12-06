# 1. What is the major difference between tuples and lists?
# Answer: Tuples are immutable whereas lists are mutable

# 2. How do you create a tuple?
t = (1,2,3)
length = len(t)
print(length)

# 3. What is unique about a set?
# answer: There can't be repeated values inside the set


list5 = [1,2,2,33,4,4,11,22,3,3,2]
set_list5 = set(list5)
print(set_list5)

# Boolean test
b1 = 2 > 3 #false
print(b1)

b2 = (3 <= 2) #false
print(b2)

b3 = (3 == 2.0) #false
print(b3)

b4 = (3.0 == 3) #true
print(b4)

b5 = (4**0.5 != 2) #false
print(b5)

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

final_value = l_one[2][0] >= l_two[2]['k1']
print(final_value) #false