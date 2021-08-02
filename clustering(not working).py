data = [0,1,3,7,10,14,16,24,30]
newData = []
cur = 0
mins = 0
for i in data:
    for j in data:
        print(i , ' ', j)
        if i != j:
            
            mins = abs(j-i)
            if len(newData) == 0:
                mins = abs(i-j)
                data.remove(j)
                data.remove(i)
                print("removed " , i, " and ", j)
                break
                pass
            elif abs(i-j) < mins:
                mins = abs(i-j)
                data.remove(j)
                data.remove(i)
                print("removed " , i, " and ", j)
                break
                pass
            newData.append(mins)

for i in newData:
    print(i)