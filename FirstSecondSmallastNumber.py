list = [5,6,7,4,2,1,45,9]
first = list[0]
for i in range(0,len(list)):
    if list[i] < first:
        first = list[i]
print("Maximum Element is : ", first)
second = list[0]
for j in range(0,len(list)):
    if list[j] != first and list[j] < second:
        second = list[j]
print("Second Best Element is : ", second)
