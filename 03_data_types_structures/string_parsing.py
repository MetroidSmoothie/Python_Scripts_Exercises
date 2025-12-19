# Log Parsing
#       When txt file is read - each line considered string, parsing begins for each line
#       Proper steps:
#       - Open file
#       - Loop over all file lines
#       - Use split() to choose which information to remove
#       - Get desired information

# Create string "Hello World", then parse to obtain only the second word:

str1 = "Hello World"

newStr = str1.split(" ")
print("^That's the new list we get from split {}".format(newStr))
for word in newStr:
    if word == "World":
        print("We found the word 'World'")
        break

str2 = "How do you do?"
newStr2 = str2.split(" ")
for word in newStr2:
    if word == "How":
        print("We found the word 'How'")
        break
