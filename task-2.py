print("---------Calculator----------")
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
op=input('Enter Operation(+,-,*,/,**):')
if op =="+":
    print("Result Of numbers =",num1+num2)
elif op =="-":
    print("Result of numbers =",num1-num2)
elif op =="*":
    print("Result of numbers =",num1*num2)
elif op =="/":
    print("Result of numbers =",num1/num2)
elif op =="**":
    print("Result of numbers =",num1**num2)
else:
    print("invlid input!")
