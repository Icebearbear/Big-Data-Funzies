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
    return data

# AVERAGE RATING FOR AN ITEM FROM U,V AND R RATINGS
def averageRating(R,V,U,I):
    totals = []
    totals.append(V[I])
    totals.append(U[I])
    avg = 0
    for i in range(len(R)):
        totals.append(R[i][I])
        if R[i][I] == R[len(R)-1][I]:
            avg = sum(totals) / len(totals)
            break
        
    print(totals)
    return avg
          
# FINDING SUPERUSER FROM INPUT U,V TO Us IN R AN OUTPUT A NEW RANKING MATRIX      
def superUser(V,U,R):
    topv,bottomv1,bottomv2,topu,bottomu1,bottomu2,cossineu,cossinev,maxu,maxv = 0,0,0,0,0,0,0,0,0,0
    current, maxRowu, maxRowv = 0,0,0 # to keep track of rows for latter use in defining which has the highest cosine similarity
    for i in range(len(R)):
        for j in range(len(R[0])):
            current = i # keep track of the current row
            
            # set all nominator and denominator for cosine similarity formula
            # add up across the colums
            topu += (U[j]*R[i][j])
            bottomu1 += math.sqrt(U[j]**2) 
            bottomu2 += math.sqrt(R[i][j]**2) 
    
            topv += (V[j]*R[i][j])
            bottomv1 += math.sqrt(V[j]**2) 
            bottomv2 += math.sqrt(R[i][j]**2) 
                    
        cossineu = topu / (math.sqrt(bottomu1) * math.sqrt(bottomu2)) # formula of Cosine Similarity
        cossinev = topv / (math.sqrt(bottomv1) * math.sqrt(bottomv2)) # formula of Cosine Similarity
        
        # find the highest cosine similarity and set the row number
        if(cossineu > maxu):
            maxu = cossineu
            maxRowu = current
        if(cossinev > maxv):
            maxv = cossinev
            maxRowv = current
                
    # find average and replace the rating with the average rating between U V and R
    for j in range(len(R[0])):        
        R[maxRowu][j] = (R[maxRowu][j] + U[maxRowu])/2
        R[maxRowv][j] = (R[maxRowv][j] + U[maxRowv])/2
    
    # return final rating matrix
    for i in R:
        print(i)   
        
def main():
    R = [[2,3,2,2,1],[2,3,1,2,2],[4,3,4,4,1],[3,2,4,1,1]]
    items = ["A","B","C","D","E"]
    V = []
    U = []
    for i in range(5):
        val = input("V input a number ")
        V.append(int(val))
        
    for i in range(5):
        val = input("U input a number ")
        U.append(int(val))
    
    item = input("select an item ")
    I = items.index(item)
    
    pairCosine(V,U)
    
    data = matrixCosine(R)
    print(data)
    
    ave = averageRating(R,V,U,I)    
    print(ave)
    superUser(V,U,R)
    
main()