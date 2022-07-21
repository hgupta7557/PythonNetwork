list=[]
long=int(input("Enter the value of index : "))
for i in range(0,long):
    print("Enter the value : ", i)
    value=int(input())
    list.append(value)
print(list)
min_element=list[0]
max_element=list[0]
for j in range(len(list)):
    if list[j] < min_element:
        min_element = list[j]
for k in range(len(list)):
    if list[k] > max_element:
        max_element = list[k]
print(min_element)
print(max_element)
