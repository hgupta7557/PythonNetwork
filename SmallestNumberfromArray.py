list=[]
long=int(input("Enter the value of index : "))
for i in range(0,long):
    print("Enter the value : ", i)
    value=int(input())
    list.append(value)
min_element=list[0]
for j in range(len(list)):
    if list[j] < min_element:
        min_element = list[j]
print(min_element)