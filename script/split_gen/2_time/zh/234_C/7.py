def maxDistance(x,y,n):
    max=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            distance=(x[i]-x[j])**2+(y[i]-y[j])**2
            if distance>max:
                max=distance
    return max**0.5
