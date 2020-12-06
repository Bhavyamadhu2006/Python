my_dict = {
  "Name" : "Bhavya" ,
  "age" : "27"}
print(my_dict)

name = my_dict["Name"]
print(name)

price = {
  "Apples" : 2.99,
  "Oranges" : 3.99,
  "Mangoes" :1.99,
  "Pomegranate" : 1.99,
  "Plums" : 4.99
}

# Know the value of any key in the following way
apple_price = price["Apples"]
print(apple_price)

# Know the items in the dictionary
items = price.items()
print(items)

# To know the keys of the dictionary
keys = price.keys()
print(keys)

# To know the values of the dictionary
values = price.values()
print(values)

get_apples = price.get("Apples")
print(get_apples)

# The value can be anything (String, number, list, another dictionary etc)
my_new_dict = {
  "k1" : 100,
  "k2" : "Countries",
  "k3" : ["States", 22, [1,2]],
  "k4" : {
    "Another Key" : "Name",
    "lists" : [100, 200, 300, "Madhu"],
    "numbers" : 12345
    }
}

print(my_new_dict)

# get the value of the numbers from the key k4
get_nested_dict = my_new_dict["k4"]["numbers"]
print(get_nested_dict)

# get the value of the string from the list in key k4 and convert it into upper case
get_lists = my_new_dict["k4"]["lists"][3].upper()
print(get_lists)