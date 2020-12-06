# Example for strings and concatenation
first_name = "Bhavya"
last_name = "Madhu Prayu"
name = first_name + " " + last_name
print(name)

# Indexing
first_index = first_name[4]
last_index = last_name[3]
index = first_index + last_index
print(index)
print(first_index)
print(last_index)

# Slicing

# This line returns the characters starting from second index till the end
first_slice = first_name[2:]

# This line returns the characters from beginning till the third index.
# So the index which we mention at last will be ignored
# In this case 4th index is ignored and displayed only till 3rd
last_slice = last_name[:4]
slicing = first_slice + " " + last_slice
print(slicing)
print(first_slice)
print(last_slice)

# slicing the sub section (avy)
sub_slice = first_name[2:5]
print(sub_slice)

upper_case = first_name.upper()
print(upper_case)

lower_case = last_name.lower()
print(lower_case)

capitals = first_name.capitalize()
print(capitals)

case_fold = last_name.casefold()
print(case_fold)
