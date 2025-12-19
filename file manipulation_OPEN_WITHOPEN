# 2 methods used: open, with open
# r = opens for reading only
# w = opens for writing only
# a = opens file for appending
# t = text, default format ("r" and "t" are assumed)
# adding a b - for binary (rb, wb, ab)


# WITH OPEN: _________
# Similar to opening file and deciding later whether to save it
# Creates context manager
# Useful when script needs to open/close file many times:
#   Can help remember to close file and manage more efficiently

with open("file.txt", "r") as file:
    data = file.read()
    print(data)

# ^ open() sets new variable to handle file
#   variable that contains file is defined after "as" ('file' in the above ex)

# OPENING / READING: _________________
f = open("demofile.txt")

# Reading file:
print(f.read())

# If file located in different location (not in same folder as Python): Must specify path
"""
f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())
"""

# To read only parts of the file (first 5 bytes/characters):
f = open("demofile.txt")
print(f.read(5))

# Reading lines of the file:
f = open("demofile.txt")
print(f.readline())
print(f.readline())

# To loop through lines of the file:    *How does this code assume we want lines read, not characters for example?*
f = open("demofile.txt")
for line in f:
    print(line)

# To close files: Needed when done using file and after opening file again w/ different permissions
f.close()

# APPENDING / WRITING: ____________

# Opening and appending
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

# Opening and overwriting
f = open("demofile.txt", "w")
f.write("I have now overwritten your file!")
f.close()

# CREATING a new file:
f = open("demofile.txt", "w")
#or
f = open("demofile.txt", "x")

# CLOSING: Saves and closes file, Best practice to always close files
close()
flush() #saves file without closing
