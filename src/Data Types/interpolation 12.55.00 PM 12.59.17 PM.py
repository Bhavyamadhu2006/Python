# String interpolation means substituting values of variables into placeholders in a string
# There are several methods to achieve string interpolation
# format() and f-strings

# String interpolation using format()
text = "This is to test"
message = "{} String {I} using {f} method".format(text, I = "Interpolation", f = "format")
print(message)

# String interpolation usinf f-strings
message1 = "Now I would like test"
full_message = f"{text} String interpolation with f-strings"
print(full_message)

# One more example for f-strings
first_name = "Bhavya"
last_name = "Madhu"
full_name = f"{first_name} {last_name}"
age = 27
details = f"{full_name} is {age} years old"
print(details)

# Add precision for float formatting
result = 100.12234
final_result = "The final result is {r:1.1f}".format(r = result)
print(final_result)

# One more example for float formatting
value = 25.23344543211348874758
precision_value = "Foramtting float result is {v:1.2f}".format(v = value)
print(precision_value)
