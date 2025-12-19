# Try: All code we want to try/handle will be set in 'try' block
# Except: If code in 'try' block fails, code will jump to 'except block to be handled

""""
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print("Result: ", result)
except:
    num3 = 5
    print(f"Cannot calculate {num1} / {num2}, next operation is {num1} + {num3}")
    sum = num1 + num3
    print(sum)
"""
# ___________________________________________________________________________
# When exception occurs, can be handled in following ways:
#   1. Print message with info about error
#   2. Continue code or redirect to function that handles error
#   3. Print error message provided by Python

""" To print Python's error message 
try:
    num1 = 10
    num2 = 0
    div = num1/num2
    print(sum)
except Exception as error:
    print(f"The following is the system's message -> {error}")
    if True:
        print("I can code whatever I want")
"""

# _____________________________________________________________________________

"""Error handling loops using 'Else', 'Finally',:
try:
    num1 = 10
    num2 = 5
    sum = num1/num2
    print(sum)
except ZeroDivisionError as error:
    print("Cannot divide by zero")
except Exception as error:
    print(f"General error - {error}")
else:
    print("No error occurred")
finally:
    print("'Finally' runs regardless")
"""
# ___________________________________________________________________________

""" Error handling using 'Raise' 
age = 13
try:
    if age < 18:
        raise Exception("The user is younger than 18")  #User defined exception is raised
except Exception as error:
    print(f"Error - {error}")
"""

# PY-04-L1 Try & Except Practice ____________________________________________

"""

num1 = int(input("Please enter a number: "))
num2 = 0
if num1 > 100:
    print("Please choose number < 100")
    num1 = (input("Please enter a number: "))
else:
    print("Thank you")

try:
    div = num1 / num2
except ZeroDivisionError:
    print(f"Cannot calculate {num1} / {num2}")
except ValueError:
    print("Something went wrong!")
    
"""
