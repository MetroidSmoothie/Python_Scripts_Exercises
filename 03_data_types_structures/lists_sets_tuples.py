# Collection = single "variable" used to store multiple values
#   List  [] = ordered and changeable. Duplicates OK
#   Set   {} = unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple () = ordered and immutable. Duplicates OK. FASTER

# [] denotes this variable as a list
# Good practice: Pluralize variables that are collections to make it more obvious
fruits = ["apple", "orange", "banana", "coconut"]

# To output specific value/element in list:
#   print(fruits[0]), print(fruits[1]), print(fruits[2]), etc.
print(fruits[0])

# To output first 3 values/elements in list:
#   print(fruits[0:3])
print(fruits[0:3])

# To output values/elements in steps:
print(fruits[::2])
