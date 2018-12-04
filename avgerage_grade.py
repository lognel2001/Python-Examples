
##Logan Nelson
##12/4/18
##avg grades


##gradelist = []
##def getGrade(gradelist):
##
##    while True:
##        maxGrade = 100
##        grade = input("Enter in a grade to exit press space bar")
##        if grade == " ":
##            break
##        elif grade.isdigit():
##            grade = float(grade)
##            if grade <= maxGrade:
##                gradelist.append(grade)
##            else:
##                q=input("are you sure this "+str(grade)+" is a good grade? y or n")
##                if q =="y":
##                    gradelist.append(grade)
##                else:
##                    print("That's not a good grade")
##        else:
##            print("That's not a good grade")
##
####getGrade(gradelist)
####print(gradelist)
##
##
##def avgfunction(gradelist):
##    total = sum(gradelist)
####    for grade in gradelist:
####        total += grade
##    avg = total / len(gradelist)
##    return avg
##
##def main(gradelist):
##
##    getGrade(gradelist)
##    avg = avgfunction(gradelist)
##    xmax = max(gradelist)
##    xmin = min(gradelist)
##    sort(gradelist)
##    print(gradelist)
##    print(xmax)
##    print(xmin)
##    print("your grade average is ",avg)
##
##main(gradelist)

start = 5
stop = 1000
stepvalue = 500
for i in range(start,stop,stepvalue):
    print(i)







