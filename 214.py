##word=input("type in a word")
##print(len(word))
##print(word.count("e"))
##print(word.find("e"),12)

##pos1 = word.find("e")
##pos2 = word.find("e",pos1+1)
##substring = word[pos1:pos2]
##print(substring)

name = input("enter in your first and last name")
x=name.find(" ")
firstName = name[:x]
lastName = name[x+1:]
#lastName = lastName.trim()
print(firstName)
print(lastName)
