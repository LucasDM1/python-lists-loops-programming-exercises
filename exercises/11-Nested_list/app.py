
coordinatesList = [[33.747252,-112.633853],[-33.867886, -63.987],[41.303921, -81.901693],[-33.350534, -71.653268]]

# Your code go here:
new=[]
for i in coordinatesList:
    for j in i:
       if i.index(j) == 1:
           new.append(j) 

for e in new:
    print(e)

