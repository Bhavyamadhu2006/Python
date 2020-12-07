# 1. Create a Statement that will print out words that start with 's'

st = 'Print only the words that start with s in this sentence'
st_list = st.split()
print(st_list)

for item in st_list:
  if item[0] == "s":
    print(item)

# 2. Print all the even numbers from 0 to 10

my_list1 = list(range(0,11,2))
print(my_list1)

# 3. Create a list of all numbers between 1 and 50 that are divisible by 3

my_list = [num for num in range(1,100) if num%3 == 0]
print(my_list)

# 4. Go through the string below and if the length of a word is even print "even!"

st1 = 'Print every word in this sentence that has an even number of letters'
st1_list = st1.split()
print(st1_list)

for item in st1_list:
  if len(item) % 2 == 0:
    print(item)

# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,100):
  if (num%3 == 0 and num%5 == 0):
    print("FizzBuzz")
  elif num%3 == 0:
    print("Fizz")
  elif (num%5 == 0):
    print("Buzz")
  else:
    print(num)

# 6. Create a list of the first letters of every word in the string below

st2 = 'Create a list of the first letters of every word in this string'
st2_list = st2.split()
print(st2_list)

first_letter_list = [item[0] for item in st2_list]
print(first_letter_list)