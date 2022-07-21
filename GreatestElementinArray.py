list=[]
long=int(input("Enter the index value : "))
for i in range(0,long):
    print("enter the value of index : ", i)
    value=int(input())
    list.append(value)
print(list)
max_element=list[0]
for j in range(len(list)):
    if list[j] > max_element:
        max_element = list[j]
print(max_element)