# 1. Build this list [0,0,0] two separate ways.

my_list = [0,0]
my_list.append(0)
print(my_list)

my_list.append(0)
print(my_list)

my_list.pop()
print(my_list)

# 2. Reassign 'hello' in this nested list to say 'goodbye' instead

list3 = [1,2,[3,4,'hello']]
list3[2][2] = "Good bye"
print(list3)

# 3. Sort the list below:

list4 = [5,3,4,6,1]
list4.sort()
print(list4)
