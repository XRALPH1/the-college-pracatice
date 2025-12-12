factor = int(input("Enter a number: "))
for u in range(1, (factor//2) + 1): #factor+1
    if factor % u == 0:
        print(u,end=" ")