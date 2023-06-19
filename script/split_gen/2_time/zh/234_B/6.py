def maxDistance():
    N = int(input())
    pointList = []
    for i in range(N):
        pointList.append(list(map(int, input().split())))
    maxDistance = 0
    for i in range(N):
        for j in range(i+1, N):
            distance = (pointList[i][0]-pointList[j][0])**2 + (pointList[i][1]-pointList[j][1])**2
            if distance > maxDistance:
                maxDistance = distance
    print(maxDistance**0.5)
maxDistance()
