total = 0
num1=int(input("Enter the Start Number of a Range : "))
num2=int(input("Enter the End Number of a Range : "))
if num2<num1:
    print("Make Sure Number 2 value is Higher than number 1")
    print("program terminated, please run it again.")
else:
    print("range number is : ", num1, num2)
for i in range(num1,num2):
    print(i)
    total = total + i
print(total)