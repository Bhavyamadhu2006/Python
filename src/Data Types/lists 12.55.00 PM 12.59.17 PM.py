# Printing the basic list
my_list = [1,2,3,4,5]
print(my_list)

# Length of the string
list_length = len(my_list)
print(list_length )

# Adding elements to the list
# This line adds 6 at the end of the element
my_list.append(6)
print(my_list)

# Adding one more element
my_list.append(7)
print(my_list)

#Removing elements from the list
#This line removes the last element
my_list.pop()
print(my_list)

#Removing particular element from the list
#This line removes the second index from the list
my_list.pop(2)
print(my_list)

#Over-writing the existing elements
my_list[1] = 100
print(my_list)