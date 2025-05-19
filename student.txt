# student details 

student_name=input("Enter the name of the student: ")
student_USN=input("Enter the USN of the student: ")
print("Enter the marks of Three subjects: ")
m1=float(input("Enter the marks of subject 1: "))
m2=float(input("enter the marks of subject 2: "))
m3=float(input("Enter the marks of subject 3: "))

Total_marks=m1+m2+m3
percentage=(m1+m2+m3)/3

print("student name: " ,student_name)
print("student USN: " ,student_USN)
print("student total marks: " , Total_marks)
print("student percentage: " , percentage)