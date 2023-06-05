def getMinDistance(s,t,x):
    minDistance = float('inf')
    for i in range(len(s)):
        if s[i] <= x:
            for j in range(len(t)):
                if t[j] <= x:
                    if s[i] + t[j] < minDistance:
                        minDistance = s[i] + t[j]
    return minDistance
