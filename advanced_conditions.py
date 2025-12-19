# PY-02-L3 Advanced Conditions

grade = int(input("Please enter a grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 65:
    print("D")
elif grade >= 0:
    print("F")
else:
    print("Invalid entry: Grade range is between 0-100")

# Notes:
# else must be last
