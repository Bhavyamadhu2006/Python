def myfunc(name):
  mystr = ""
  for item in name:
    if name.index(item)% 2 != 0:
      mystr += item.lower()
    else:
      mystr += item.upper()
  return mystr

result = myfunc("bhavya")
print(result)
