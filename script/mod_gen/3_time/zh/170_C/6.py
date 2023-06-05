def getClosestNumber(x, p):
    p.sort()
    #print(p)
    if x in p:
        return x
    if x < p[0]:
        return p[0]
    if x > p[-1]:
        return p[-1]
    for i in range(len(p)-1):
        if x > p[i] and x < p[i+1]:
            return p[i] if abs(p[i]-x) < abs(p[i+1]-x) else p[i+1]

if __name__ == '__main__':
    getClosestNumber()