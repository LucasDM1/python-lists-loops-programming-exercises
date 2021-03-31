parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

def get_parking_lot(parking_state):
    state={}
    occupied=0
    available=0
    total=0
    for arr in parking_state:
        for i in arr:
            if i == 1:
                occupied+=1
                
            elif i == 2:
                available+=1
                
    total=occupied+available
    state["total_slots"]=total
    state["available_slots"]=available
    state["occupied_slots"]=occupied
    
    return state
    
#Your code go here:

print(get_parking_lot(parking_state))
