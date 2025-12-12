count=0
factor = int(input("Enter a number: "))
for i in range(1, factor + 1):#(factor//2)+1
    if factor % i == 0:
      count=count+1
print(count)