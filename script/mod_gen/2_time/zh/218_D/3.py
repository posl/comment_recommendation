def getRectNum(pointList):
    rectNum = 0
    for i in range(len(pointList)):
        for j in range(i+1, len(pointList)):
            if pointList[i][0] < pointList[j][0] and pointList[i][1] < pointList[j][1]:
                if [pointList[i][0], pointList[j][1]] in pointList and [pointList[j][0], pointList[i][1]] in pointList:
                    rectNum += 1
            elif pointList[i][0] > pointList[j][0] and pointList[i][1] > pointList[j][1]:
                if [pointList[i][0], pointList[j][1]] in pointList and [pointList[j][0], pointList[i][1]] in pointList:
                    rectNum += 1
    return rectNum

if __name__ == '__main__':
    getRectNum()