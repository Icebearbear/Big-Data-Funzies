###### WARNING #########
###### CODE IS PARTIALLY WORKING #######
###### NEED FIXING ON LINE 27 AND 28 WHERE THE LOGIC OF CHOOSING CLUSTER IS ######
file = open(r"C:\Users\Acer\Documents\kool_stuff\Big-Data-Funzies\test.txt")
centroids = [[1,0,0] , [2,4,0]]   

def calculate_centroids(cluster, ind):
    print(ind)
    
    # set initial centroids
    first_centroid = centroids[ind][0] 
    second_centroid = centroids[ind][1]
    if len(cluster) > 1:
        for i in range(len(cluster[ind])):
            # calculate new centroid 
            first_centroid = (first_centroid + cluster[ind][i][0])/len(cluster[ind])
            second_centroid = (second_centroid + cluster[ind][i][1])/len(cluster[ind])
    # replace the old centroid    
    centroids[ind] = [first_centroid, second_centroid, centroids[ind][2]+1]    

def main():
    sortedFile = []
    for i in file:
        sortedFile.append([float(i.split()[0]), float(i.split()[1])])
    sortedFile.pop(0)
    sortedFile = sorted(sortedFile) 
    cluster = [[],[]] # empty array for 2 cluster
    ind = 0
    for i in range(len(sortedFile)):
        # choose which centroid the node is closer to
        if abs(sortedFile[i][0] - centroids[0][0]) < abs(sortedFile[i][0] - centroids[1][0]) or abs(sortedFile[i][1] - centroids[0][1]) < abs(sortedFile[i][1] - centroids[1][1]):
            cluster[0].append([sortedFile[i][0], sortedFile[i][1]])
            ind = 0
        else:
            cluster[1].append([sortedFile[i][0], sortedFile[i][1]])
            ind = 1
        calculate_centroids(cluster, ind)
        print(centroids)
    return centroids
   
print(main())  