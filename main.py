#Write a program to check if the number entered by the user is an Armstrong number or not?
sum=0
number=int(input("Plesse enter a number"))
originnumber=number
digit=int(input("How many digits are the in you number"))

while number>0:
    n=number%10
    n=n**digit
    sum=sum+n
    print(sum)
    number=number//10
if sum==originnumber:
    print("it is an amstrung number ")
else:
    print("not an amstrung number")
