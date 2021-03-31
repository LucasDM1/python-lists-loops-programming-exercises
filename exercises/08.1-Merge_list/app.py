chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    arr=[]
    #Your code go here:
    for one in list1:
        arr.append(one)
    for two in list2:
        arr.append(two)
    return arr
    
print(merge_list(chunk_one, chunk_two))
