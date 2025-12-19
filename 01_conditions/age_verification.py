# Lab PY-02-L2 | Create script that checks if users can legally purchase an alcoholic beverage

# Create variables for name and age - Use input() function to get user input:
name = input("What is your name")
age = input("What is your age")

# Use int() function to cast variable AGE from string to an integer
age = int(age)

# Can also consolidate the above by: age = int(input("Enter your age: "))

# Print greeting containing user's name and age. Use format method to insert variables
print ("Hello {}, your age is {}" .format(name, age))

# Create an if-else statement to check if user old enough tot purchase alcohol and print appropriate message
if age >= 21:
    print("You can buy an alcoholic beverage")
else:
    print("Go home")

#______________________________________________

HRV = input("What was your HRV this morning?")
HRV = int(HRV)

if HRV > 4:
    print("You can train today")
else:
    print("You should not train today")
