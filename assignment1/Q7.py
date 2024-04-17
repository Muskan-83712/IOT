#Using for loop, write and run a Python program to find factorial from 0 to 10
for num in range(11):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial*num
        print(f"the factorial of {num} is {factorial}")