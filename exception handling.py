
##while True:
##    try:
##        num = float(input("Enter a number: "))
##        break
##    except:
##        
##        print("Something went wrong!")
##
##print(num)

##try:
##    num = float(input("\nEnter a number: "))
##except ValueError:
##    print("That was not a number!")
##except NameError:
##    print("That was a name error")

##for value in (None, "Hi!"):
##    try:
##        print("Attempting to convert", value, "-->", end=" ")
##        print(float(value))
##        except(TypeError):
##            print("Something went wrong! type error")
##        except(ValueError):
##            print("Something went wrong! value error")    

##try:
##    num = float(input("\nEnter a number: "))
##except ValueError as e:
##    print("That was not a number! Or as Python would say....")
##    print(e)

try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number", num)
