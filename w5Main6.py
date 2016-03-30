marks=raw_input("input marks: ")
def computerGrade(marks):
    if(90<=marks<=100):
        grade="A"
    elif(80<=marks and mark<90):
        grade="B"
    elif(70<=marks and mark<80):
        grade="C"
    elif(60<=marks and mark<70):
        grade="D"
    elif(60<=marks):
        grade="F"
    return grade
result=converGrade(marks)
print "Grade is %s" %result