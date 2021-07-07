file = open(r"C:\Users\Acer\Documents\kool_stuff\Big-Data-Funzies\ca-netscience.txt")
import math
sortedFile = []
for i in file:
    sortedFile.append(i.split())
fileRange = int(sortedFile[0][2]) 
sortedFile.pop(0)

matrix = [[0 for column in range(0,fileRange)] for row in range(0,fileRange)]

for i in sortedFile:
    matrix[int(i[2])-1][int(i[1])   -1] = 1

class ShortestPath():
    def __init__(self, nodes, matrix):
        self.nodes = nodes  # no of nodes = 398
        self.matrix = matrix # the matrix of edges
    
    def minimumDistance(self, dist, visited):
        min = float("inf")
        minNode = 0
        # print(visited[0])
        for i in range(self.nodes):
            # print(i)
            # print(dist[i] ," ", visited[i] )
            if dist[i] < min and visited[i] == False:
                # print('mion', i)
                min = dist[i]
                minNode = i 
                # print(i)
        # print(minNode)    
        return minNode
    
    def analysis(self, src):
        
        dist = [float('inf')] * self.nodes # set distance of all nodes as infinity
        visited = [False] * self.nodes  # start with all nodes unvisited 
        
        dist[src] = 0 # base case - distance from source to source = 0
        for n in range(self.nodes):
            minNode = self.minimumDistance(dist,visited)
            visited[minNode] = True
            # examine its unvisited neighbours
            for i in range(self.nodes):
                # print(matrix[minNode][i], " ", visited[i] )
                if matrix[minNode][i] > 0 and visited[i] == False and dist[i] > dist[minNode] + self.matrix[minNode][i] :
                    dist[i] = dist[minNode] + self.matrix[minNode][i]
                    # print(dist[i])
                
                # print(dist[ind] , " " , ind)
        return dist
        # print(visited)

                    
x = ShortestPath(fileRange, matrix)
x.analysis(0) # 0 as the source
# def minStep (n):
#         #complete the function 
#         # min = 1
#     steps = 0
#     current = n
#     data = []

#     for i in range(n, -1,-2):
#         next = i
#         # print((current/next))
#         if next % 3 == 0 or next == current+1:
#             data.append([current, next , 1])
#             current = next
#     matrix2 = [[0 for column in range(0,len(data))] for row in range(0,len(data))]
    
#     # for i in sortedFile:
#     #     matrix2[int(i[2])-1][int(i[1])   -1] = 1
#     dist = [float("inf")] * len(data)
#     visited = [False] * len(data)
#     dist[0] = 0
    
#     for i in range(len(data)):
#         min = float("inf")
#         min_index = 0
#         if dist[i] < min and visited[i] == False:
#             min = dist[i]
#             min_index = i
#         visited[min_index] = True
#         # print(n, min_index,  len(data))
#         for i in data :
#             print(i)
#         for j in range(len(data)):
#             print(dist[j] ," ", data[min_index][j], " ", visited[j])
#             if  data[min_index][j] > 0 and visited[j] == False and dist[j] > dist[min_index] + data[min_index][j]:
#                 dist[j] = dist[min_index] + data[min_index][j]
    
#     return ""
    
# print(minStep(379))