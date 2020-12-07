# 1. Using keys and indexing, grab the 'hello' from the following dictionaries

d = {'simple_key':'hello'}
d['simple_key']
print(d)

valu_of_d = d.values()
print(valu_of_d)


my_dict = {'k1':{'k2':'hello'}}
value_of_hello = my_dict["k1"]["k2"]
print(value_of_hello)

# Getting a little tricker
d1 = {
  'k1':[
     {
      'nest_key':['this is deep',['hello']]
     }
    ]
  }
value_of_last_key = d1["k1"][0]["nest_key"][1][0]
print(value_of_last_key)

# This will be hard and annoying!
d2 = {
  'k1':
    [
      1,
      2,
      {'k2':
        ['this is tricky',
         {'tough':[1,2,['hello']]}
        ]
      }
    ]
  }

index_value = d2["k1"][2]["k2"][1]["tough"][2][0]
print(index_value)

# 2.  Can you sort a dictionary? Why or why not?
# Answer: We cannot sort dictionaries, as they will have the values based on key and value pairs
# And the elements inside the dictionaries are unsotred and we don't have to remember the index value of the object
