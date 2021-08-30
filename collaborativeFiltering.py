import math 

# FIND COSSINE SIMILARITY BETWEEN V AND U
def pairCosine(V, U):
    top, bottom1, bottom2 = 0,0,0
    for i in range(len(V)):
        top = top + (V[i] * U[i])
        bottom1 = bottom1 + (V[i]**2)
        bottom2 = bottom2 + (U[i]**2)
        
    cossine = top / (math.sqrt(bottom1) * math.sqrt(bottom2)) # formula of Cosine Similarity
    print("Cossine Similarity between V and U is " + str(cossine))
        
# FIND COSSINE SIMILARITY FOR R
def matrixCosine(R):  
    data = []
    keys = []
    top, bottom1, bottom2 = 0,0,0
    for i in range(len(R)):
        for j in range(len(R)): # go through every combination among rows
            for k in range(len(R[0])): # and go through each column
                if k == 0:
                    top, bottom1, bottom2 = 0,0,0

                top = top + R[i][k] * R[j][k]
                bottom1 = bottom1 + R[i][k]**2
                bottom2 = bottom2 + R[j][k]**2 
                
            cossine = top / (math.sqrt(bottom1) * math.sqrt(bottom2))
        
            data.append([[i,j] , cossine])
            keys.append([i,j])
            # else:    
            #     for l in range(len(data)):
            #         print(l)
            #         # print(i ," ", l[0], " " ,j," ", l[0])
            #         if i == data[l][0] and j == data[l][0]:
            #             print("no")
            #             # pass
            #             break
            #         else:
            #             data.append([[i,j] , cossine])
            #             # pass
            #             break
            # # print(data[0])
            
def main():
    R = [[2,3,2,2,1],
    [2,3,1,2,2],
    [4,3,4,4,1],
    [3,2,4,1,1]]
    V = []
    U = []
    for i in range(5):
        val = input("V input a number ")
        V.append(int(val))
        
    for i in range(5):
        val = input("U input a number ")
        U.append(int(val))
    
    pairCosine(V,U)
    matrixCosine(R)
    
    # for d in data:
    #     print(d)
                