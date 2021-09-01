R = [[1,0,1,0,1],
     [1,1,1,1,1],
     [1,0,0,0,1]]

def jaccard():
    top,bottom,sim,simMax,current,maxRows = 0,len(R),0,0,0,0
    for i in range(len(R)):
        for j in range(len(R)):
            for k in range(len(R[0])):
                if i == j :
                    break
                current = [i,j]
                if k == 0:
                    top,bottom=0,len(R[0])
                if R[i][k] == 0 and R[j][k] == 0:
                    bottom -= 0
                else:
                    if R[i][k] == 1 and R[j][k] == 1:
                        top += 1
                                          
            sim = top / bottom
            if sim > simMax:
                simMax = sim
                maxRows = current
    
    for i in range(len(R[0])):
        R[maxRows[0]][i] = (R[maxRows[0]][i] + R[maxRows[1]][i])/2
                        
    return R            

print(jaccard())