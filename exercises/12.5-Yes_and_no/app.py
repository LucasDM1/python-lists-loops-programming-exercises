theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def app(elem):
   
    if elem == 1:
        return "wiki"
    else:
        return "woko"

wikiwoko=list(map(app, theBools))



print(wikiwoko)