# typecasting = The process of converting a value of one data type to another
#               (string, integer, float, boolean)
#               Explicit vs Implicit


name = "Bro"
age = 21
gpa = 1.9
student = True

# To find datatype of a variable:
#   type(variable) / ex:type(name)
#   Must place above statement within a print statement to output datatype:
#   print(type(variable)) / ex: print(type(name))
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# Explicit conversion (manually converting into different datatype)

# Need to convert variable 'age' to 'float'
# Reassign variable age with = then explicitly cast age into float:
# age = float(age)
# print(age) / print(type(age)) to confirm age value and datatype
age = float(age)
print(age)
print(type(age))

# Typecasting something as a boolean [name = bool(name)] can be useful to determine user input
# Ex: Casting name as a boolean will return TRUE with user input in name value (name = "Bro")
#       Will return FALSE with no user input in name value (name = "")
#       Even a space will register a TRUE

#Implicit conversion (automatic conversion)

# x = 2
# y = 2.0
# x is an integer, y is a float
# If we do x = x / y - The result will return as a float (even though we defined x as an integer)
