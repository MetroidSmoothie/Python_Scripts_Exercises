# dictionary = a collection of {key:value} pairs
#              Example of key:value pairs: Name:ID, Item:Price Age:Number
#              Ordered and changeable
#              No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Dehli",
            "China": "Beijing",
            "Russia": "Moscow"}
# ^ Creates dictionary called 'capitals' with keys being Country and values being Capitals
# To list functions of dictionaries: print(dir(capitals)) - list of functions
#                                    print(help(capitals)) - description of functions

# To get a value from the dictionary: [dictionary].get("key")
capitals.get("USA")
print(capitals.get("USA"))

# By default if key not in dictionary, will return NONE
# Can use in if statement (whether capital exists in dictionary or not)
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital does not exist")

# To update/change dictionary: [dictionary].update({"Key": "Value"}
capitals.update({"Germany": "Berlin"})

# To remove a key:value pair: [dictionary].pop("Value)
capitals.pop("China")

# To remove latest key:value entry: [dictionary].popitem()
# To clear the dictionary: [dictionary].clear()

# To get all of the keys in a dictionary, but not the values: [dictionary].keys()
#       Can assign a variable to keys: keys = capitals.keys() - print(keys)
#       Output will be an OBJECT, that resembles a list
keys = capitals.keys()
print(keys)

# Can use a for loop with keys to iterate through keys in a dictionary:
#       "For every key in capitals using the .key method, we will print every key:

#       for key in capitals.keys()
#       print(key)


# To get all of the values in a dictionary, but not the keys: [dictionary].values()
#       Can assign a variable to keys: values = capitals.values() - print(values)
#       Output will be an OBJECT, that resembles a list
values = capitals.values()
print(values)

# Items method: Returns a dictionary object that resembles a 2D list of tuples - items = [(), (), ()]
#       items = capitals.items()
# For every key, and value in capitals.items method
#       Will print every key value pair using f" string to format to key:value
for key, value in capitals.items():
    print(f"{key}: {value}")
