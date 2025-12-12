factor = int(input("Enter a number: "))
count = 0
for i in range(1, factor + 1):#(factor//2)+1
    if factor % i == 0:
      count=count+1
if count == 2:
    print(factor,"is a Prime number")
else:
    print(factor,"is Not a Prime number")
