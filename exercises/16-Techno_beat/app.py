def lyrics_generator(arr):
    aux=[]
    counter=1
    str1=""
    for i in range(0, len(arr)):
        if arr[i] == 1:
            if counter==3:
                aux.append("Drop the base !!!Break the base!!! " )
                counter=0
            else:
                aux.append("Drop the base ")
                counter+=1
        else:
            aux.append("Boom ")
    return str1.join(aux)
        


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))