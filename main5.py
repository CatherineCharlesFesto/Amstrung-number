# create a list of square values of numbers between a specific range by the user then separate odd and even
start=int(input("Enter the start of the range: "))
end=int(input("Enter the end of the range: "))
squares=[i**2 for i in range(start,end+1)]
odd_squares=[i for i in squares if i%2!=0]
even_squares=[i for i in squares if i%2==0]
print("Odd squares:",odd_squares)
print("Even squares:",even_squares)
