name=input("enter your name:")
yearofbirth=int(input("enter the year of the your birth:"))
currentyear=int(input("enter the current year:"))

age=currentyear-yearofbirth

if(age>60):
     print(name,"your are",age,"year old.you are senior citizen:")
else:
     print(name,"your are",age,"year old.you are not senior citizen:")