def findHash(strList):
    #print(strList)
    for i in range(10):
        for j in range(10):
            if strList[i][j] == "#":
                return i,j
