num = int(input("Enter the number to check the prime : "))
flag = False
if num <= 1:
    print("This is not part of prime number's Race : ", num)
else:
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                flag = True
                break
        if flag:
            print("number is not prime : ", num)
        else:
            print("number is prime : ", num)