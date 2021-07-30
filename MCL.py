graph = [[0,1,0],
         [1,0,1],
         [0,1,0]]
identity = [[1,0,0],
            [0,1,0],
            [0,0,1]]

selfLoop = [[0 for column in range(len(graph))] for row in range(len(identity[0]))]
transitionMatrix = selfLoop.copy()
sumCol = 0
r = 2
p = 2
for i in range(len(graph)):
    for k in range(len(graph)):
        sumCol = sumCol + (graph[k][0]) # transition matrix - sum of each column
    for j in range(len(identity)):
        # print(i, j)
        selfLoop[i][j] = graph[i][j] + identity[i][j] # self loop - add adjecent matrix to identity matrix 
        # print(graph[j][i], sumCol) 
        transitionMatrix[j][i] = graph[j][i]/sumCol # transition matrix - each element over sum of each column

normalisedMatrix = transitionMatrix.copy()        
for i in range(len(transitionMatrix)):
    for k in range(len(transitionMatrix)):
        sumCol = sumCol + (transitionMatrix[k][0])**r
    for j in range(len(transitionMatrix[0])):
        normalisedMatrix[j][i] = transitionMatrix[j][i]**r/sumCol 

result = [[0 for column in range(len(transitionMatrix))] for row in range(len(transitionMatrix[0]))]

# M^2 = M*M
for i in range(len(transitionMatrix)):
    for j in range(len(transitionMatrix[0])):
        result[i][j] += transitionMatrix[i][j] * transitionMatrix[j][i]

# next step is to continuously calculate M^2 until the matrix converges
# then that is the final clustering

