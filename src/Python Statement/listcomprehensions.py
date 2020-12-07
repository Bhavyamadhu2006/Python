mystring = "hello"
mylist = []

for letter in mystring:
  mylist.append(letter)

print(mylist)

# using list comprehensions

mystring2 = "World"
mylist1 = [letter for letter in mystring2]
print(mylist1)

# Another example

my_nums = [num for num in range(0,20) if num%5 == 0]
print(my_nums)

# One more example

value = [x*y for x in [1,2,3] for y in [10,100,1000]]
print(value)

# Last one

results = ["Fizz - {}".format(num) for num in range(0,10) if num%5 == 0]
print(results)

