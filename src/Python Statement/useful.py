from random import shuffle,randint

# Range funtion

for x in range(1,100):
  if x%5 == 0:
    print(x)

for num in range(0,11,2):
  print(num)

list1 = list(range(5,10))
print(list1)

# Enumerate function

index_count = 0
word = "abcde"

for item in word:
  print(word[index_count])
  index_count += 1

for item in enumerate(word):
  print(item)

for x,y in enumerate(word):
  print(x)
  print(y)
  print("\n")

# Zip function

first_list = [1 ,2 , 3]
second_list = [10, 100, 1000]

for item in zip(first_list,second_list):
  print(item)

for x,y in zip(first_list, second_list):
  print(x*y)

for x in first_list:
  for y in second_list:
    print(x*y)

# in operator

boolean = 1 in [1,2,3,4,5]
print(boolean)

boolean1 = "x" in [1,2,3,4,5]
print(boolean1)

# Mathematical functions
list1 = [1,2,3,4,5]

min_val = min(list1)
max_val = max(list1)
print(min_val)
print(max_val)

# Shuffle function in random library

my_list_1 = [1,7,3,6,5,4,9,2,4,8]
shuffle(my_list_1)
print(my_list_1)

# Randint function in random

result = randint(0,10)
print(result)

# input function

result1 = input("Enter a number here: ")
print(result1)