'''2] Write a program to accept a 4 digit number and
a. Display face value of each decimal digit
b. Display place value of each decimal digit
c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
ut should be
a. 9 3 6 1
b. 9361 = 9 000 + 300 + 60 + 9
c. 1639'''

num = int(input("Enter a four digit number : "))

d = num%10
num = num/10

c = int(num%10)
num = num/10

b= int(num%10)
num = num/10

a= int(num)

print(f"face value of decimal digit:")
print(f"{a} {b} {c} {d}")

print(f"place value of decimal integer:")
print(f"num = {a*1000} {b*100} {c*10} {d*1}")

print(f"reverse number = {d}{c}{b}{a}")