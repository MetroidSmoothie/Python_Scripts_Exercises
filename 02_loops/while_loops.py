# while loop = execute some code WHILE some condition remains true

# Say we want to prompt user to enter their name, and continue to prompt them if they do not
# If "" condition is not true, while loop will be exited. Almost like an if statement but instead of executing
#       some code once, potentially executes infinitely

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")       # This reprompt is the exit strategy

print(f"Hello {name}")

# Asking for users age:

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"Wow, you look great for {age}!")

# not logical operator

food = input("Enter a food you like (q to quit) ")

while not food == "q":                          # Says print "" when food does not == "q"
    print(f"Glad you like {food}")
    food = input("Enter another food you like (q to quit) ")

print("Bye!")

# Or logical operator

num = int(input("Enter a # between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 and 10: "))

print(f"Your number is {num}")
