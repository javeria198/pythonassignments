print("*****Marksheet*****")
n1 = int(input("Enter marks of english:"))
n2 = int(input("Enter marks of chemistry:"))
n3 = int(input("Enter marks of computer:"))
n4 = int(input("Enter marks of sindhi:"))
n5 = int(input("Enter marks of pak studies:"))

avg = ((n1+n2+n3+n4+n5)/425)*100

print(avg)    
if avg>80:
    print("Grade A+")
elif 80>=avg>=70:
    print("Grade A")
elif 70>=avg>=60:
    print("Grade B")    
elif 60>=avg>=50:
    print("Grade C")    
elif 50>=avg>=40:
    print("Grade D") 
else:
    print("Grade F")       