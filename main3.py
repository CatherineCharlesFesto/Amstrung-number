#Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.
empty_list=[]
print("empty_list:", empty_list)
num=[10,20,30,40,50]
sum=0
for i in num:
    sum=sum+i
print("sum is:",sum)
avarage=sum/len(num)
print("avarage is:",avarage)
num.sort()
print("smallest number is:",num[0])
print("largest number is:",num[-1])
