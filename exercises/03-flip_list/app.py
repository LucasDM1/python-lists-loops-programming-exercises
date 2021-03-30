arr = [45, 67, 87, 23, 5,  32, 60]

new_list=[]
first= len(arr)-1
print(first)
for i in range(first, -1, -1):
    new_list.append(arr[i])
print(new_list)