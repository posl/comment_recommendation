def getK(k):
    if k%2==0 or k%5==0:
        return -1
    else:
        x=0
        for i in range(1,k+1):
            x=x*10+7
            if x%k==0:
                return i
        return -1
