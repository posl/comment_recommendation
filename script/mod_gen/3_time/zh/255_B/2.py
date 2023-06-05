def getLight(n, k, a, x, y):
    maxR = 0
    for i in range(k):
        for j in range(i+1, k):
            r = ((x[a[i]-1]-x[a[j]-1])**2 + (y[a[i]-1]-y[a[j]-1])**2)**0.5
            if r > maxR:
                maxR = r
    return maxR

if __name__ == '__main__':
    getLight()