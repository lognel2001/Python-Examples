
import random
name= input("enter your name")
print(name[0])#"b" is the 10th character in "Eric Broadbent", it's also the -4th character
length = len(name)
print(length)
index_pos = random.randrange(0, length)
if index_pos<= length:
    char = name[index_pos]
    print(char)
else:
    print("that's out of the range")
