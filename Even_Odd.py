num=int(input("Enter a value to check Even or Odd: " ))
print("Entered number is : ", num)
if num==0:
    print(num, " is not considered")
elif num%2==0:
    print(num, "Entered number is Even ")
else:
    print(num, "Entered number is odd")