#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
def randomNum():
    
    for i in range(10):
        ran= random.randint(0, 100)
        my_list.append(ran)
        i+=i
    return my_list
print(randomNum())