print("welcome to student result profile :-")
name=input("enter student name:-")
age=input("enter student age:-")
course=input("enter student course:-")

sub1=input("enter subject1 name:-")
marks1=int(input("enter student marks:-"))

sub2=input("enter subject2 name:-")
marks2=int(input("enter student marks:-"))

sub3=input("enter subject3 name:-")
marks3=int(input("enter student marks:-"))

sub4=input("enter subject4 name:-")
marks4=int(input("enter student marks:-"))

sub5=input("enter subject5 name:-")
marks5=int(input("enter student marks:-"))

sub6=input("enter subject6 name:-")
marks6=int(input("enter student marks:-"))

total=marks1+marks2+marks3+marks4+marks5+marks6
percentage=(total/600)*100


print("\n----- STUDENT RESULT -----")

print("student name:-",name)
print("student age:-",age)
print("course:-",course)
print(sub1,":",marks1)
print(sub2,":",marks2)
print(sub3,":",marks3)
print(sub4,":",marks4)
print(sub5,":",marks5)
print(sub6,":",marks6)
print("total marks:-",total)
print("percentage:-",percentage)
if percentage>=65:
    print("Grade:-first division",percentage)
elif percentage>=55:
    print("Grade:-second division",percentage)
elif percentage>=33:
    print("Grade:-third division",percentage)
else:
    print("Grade:-Fail",percentage)