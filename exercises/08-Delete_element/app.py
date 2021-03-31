people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    arr=[]
    for person in people:
        if person_name != person:
            arr.append(person)
    return arr

    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))