x = 0

while x<5:
  print(x)
  x += 1
else:
  print("X is no more less than 5")

# Break, continue and pass
# pass
x = [1,2,3]

for item in x:
  pass
print("End of Script")

# Continue

name = "Bhavya Madhu"

for letter in name:
  if letter == "a":
    continue
  print(letter)

# break
name1 = "Prayushi"

for letter in name1:
  if letter == "s":
    break
  print(letter)