def party_function(function):
    if (function == "wedding"):
      return "Happy Anniversary"
    elif (function == "Birthday"):
      return "Happy Birthday"
    elif (function == "Craddle ceremony"):
      return "God bless"
    else:
      return "Good wishes"

result = party_function("wedding")
print(result)

# for loop function
def check_list(name):
  my_name = []

  for letter in name:
    my_name.append(letter)
  return my_name

result = check_list("Bhavya")
print(result)
