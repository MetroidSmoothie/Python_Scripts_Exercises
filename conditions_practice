# if = Do some code only IF some condition is TRUE
#       Else = do something else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up")
# ^ This elif statement will not be reached even if someone inputs a condition that is TRUE (input 111 y/o)
# This is because it technically meets the first if age >= 18
# Code should be rewritten as:
#   If age >= 100 print("You are too old to sign up")
#   Elif age >= 18: print("You are now signed up!")
else:
    print("You must be 18+ to sign up")

# elif: Just adds another condition / checks another condition
# else when using elif: If no above conditions are true, do this

#___________
# Example:

response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food!")
# == is the comparison operator (Will compare if 2 values are equal)
# = is the assignment operator, will assign value to a variable
else:
    print("No food for you!")

#___________
# Example:

name = input("Enter your name: ")
if name == "":
    print("Please input a name value")
else:
    print(f"Hello {name}")

#___________
# Use of Booleans with IF statements

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")
# ^Can use Boolean variable (for_sale) in place of condition. So if for_sale means if for_sale is TRUE then print...
# Changing the value of for_sale from TRUE to FALSE will determine what string is outputted
