def get_triangles(sticks):
    sticks.sort()
    triangles = []
    for i in range(len(sticks)):
        for j in range(i+1,len(sticks)):
            for k in range(j+1,len(sticks)):
                if sticks[i] + sticks[j] > sticks[k]:
                    triangles.append([sticks[i],sticks[j],sticks[k]])
                else:
                    break
    return triangles
