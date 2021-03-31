#Import random
import random

ran=random.randint(1, 5)
print(ran)
#Create the function below:
def matrixBuilder(size):
    matrix=[]
    bigger=[]
    for i in range(size):
        matrix.append(1)
    
    for j in range(size):
            bigger.append(matrix)

    print(bigger)
    return bigger

matrixBuilder(ran)
