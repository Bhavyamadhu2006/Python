# For loops
States = ["New York", "Colorado", "Nevada", "Arizona", "Wyoming", "Utah", "Florida"]

for state in States:
  print(state)

# Another Example
my_list = [1,2,3,4,5,6,7,8,9,10]

for item in my_list:
  if (item % 2) != 0:
    print(item)

# Example 3
for letter in "Hello World":
  if (letter != "o"):
    print(letter)

# Fourth Example
for x in range(0,50):
  if (x%3) == 0:
    print(x)

# Next Example
list1 = [1,2,3,4,5,6,7,8,9,10]
list_count = 0

for num in list1:
  list_count = list_count + num
print(list_count)

# For loops for tuples
mylist = [(1,2), (3,4), (5,6), (7,8)]

for item in mylist:
  print(item)

# Can also do in this way
mylist1 = [(1,2), (3,4), (5,6), (7,8)]

for (a,b) in mylist1:
  print(a)
  print(b)

# Dictionary for loop
d = {"k1": 1, "k2": 2, "k3": 3}

for items in d.items():
  print(items)

for key, value in d.items():
  print(value)

for value in d.values():
  print(value)

for key in d.keys():
  print(key)