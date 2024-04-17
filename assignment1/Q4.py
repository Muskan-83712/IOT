#4] Write a Python function to find the maximum of three numbers.

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

def max(n1,n2,n3):    
    if (n1 > n2) | (n1 > n3):
        print(f"num1 is greater")
    elif n2>n3:
        print(f"num2 is greater")
    else :
        print(f"num3 is greater")

max(num1,num2,num3)