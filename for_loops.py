# for loops = execute a block of code a FIXED number of times.
#             Can iterate over a range, string, sequence (list, tuple), etc.
#             Tend to be better in situations where we need to do something only a fixed number of times

# Range: Suppose we need to count to 10:
for x in range(1, 11):      # x is counter
    print(x)                # This line defines the code we want to repeat for the specified amount of times

# Range: Count down from 10 with a message when for loop escaped
for x in reversed(range(1, 11)):       # enclose range in reversed function to count backwards
    print(x)

print("HAPPY NEW YEAR!!")

# Range: Print 1 - 11 but use step function to count by 2's (Add 2 to range)
for x in range(1, 11, 2):
    print(x)

# String: Credit card number
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# Useful key words:
    # Continue: Will skip over defined iteration (Skipping over unlucky 13)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

    # Continue: Will break out of loop
for x in range(1, 27):
    if x == 13:
        break
    else:
        print(x)
