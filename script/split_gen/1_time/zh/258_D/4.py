def getMinTime(N,X,AB):
    if N == 1:
        return AB[0][0] + AB[0][1] * X
    else:
        minTime = AB[0][0] + AB[0][1] * X
        for i in range(1,N):
            time = AB[i][0] + AB[i][1] * X
            if time < minTime:
                minTime = time
        return minTime
