#6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function 
#accepts the number as an argument.

def factorial(n):
    if n < 0:
        print("Enter a non-negative integer: ")
    elif n == 0:
        return 1
    else :
        return (n *factorial(n-1))

num = int(input("Enter the number: "))

fact = factorial(num)
print(f"the factorial of {num} is {fact}")