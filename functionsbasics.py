def viewPrograms():
    print("1. Prime number program")
    print("2. Reverse of a given number")
    print("3. Print factors of a given number")
    option=int(input("Choose your option: "))
    if option==1:
        isPrime()
    elif option==2:
        reverseNumber()
    elif option==3:
        factors()
    else:
        print("Please select 1 to 3")


def isPrime():
  factor1 = int(input("Enter a number: "))
  count = 0
  for i in range(1, factor1 + 1):
    if factor1 % i == 0:
      count = count + 1
  # The check for primality should happen after the loop completes
  if count == 2:
    print(factor1,"is a Prime number")
  else:
    print(factor1,"is Not a Prime number")


def reverseNumber():
  num=int(input("Enter your number: "))
  rev=0 # Corrected indentation
  original_num = num # Store original num for printing
  while num!=0: # Corrected indentation
    rem=num%10
    rev=rev*10+rem
    num=num//10
  print("Reverse number of", original_num, ": ",rev) # Corrected indentation

def factors():
  factor = int(input("Enter a number: "))
  print("Factors of", factor, ":", end=" ")
  for u in range(1, factor + 1): # Corrected range to include the number itself
    if factor % u == 0:
        print(u,end=" ")
  print() # Add a newline for better output formatting


viewPrograms()