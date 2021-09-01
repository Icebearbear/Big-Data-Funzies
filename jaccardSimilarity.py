R = [[1,0,1,0,1],
     [1,1,1,1,1],
     [1,0,0,0,1]]

def jaccard():
    top,bottom,sim,simMax,current,maxRows = 0,len(R),0,0,0,0
    for i in range(len(R)):
        for j in range(len(R)):
            for k in range(len(R[0])):
                # avoid comparing to the same row
                if i == j :
                    break
                
                # keep track of the current two rows 
                current = [i,j]
                
                # at the start of new row, set to initial state
                if k == 0:
                    top,bottom=0,len(R[0])
                
                # minus away if there is no union between user, both 0
                if R[i][k] == 0 and R[j][k] == 0: 
                    bottom -= 0
                
                # if both 1 , add to nominator
                else:
                    if R[i][k] == 1 and R[j][k] == 1:
                        top += 1
                                          
            sim = top / bottom
            if sim > simMax:    # set maximum similarity after each row
                simMax = sim
                maxRows = current
    
    # set first row to be new ratings with average between two similar user --> superuser
    for i in range(len(R[0])):
        R[maxRows[0]][i] = (R[maxRows[0]][i] + R[maxRows[1]][i])/2
        
    # remove the second row
    del R[maxRows[1]]
                        
    return R            

print(jaccard())