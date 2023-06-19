def getPermutation(string, k):
    #print(string)
    if len(string) == 1:
        return string
    else:
        string = sorted(string)
        n = len(string)
        #print(string)
        #print(k)
        m = 1
        for i in range(1, n):
            m *= i
        #print(m)
        if k % m == 0:
            i = k // m - 1
        else:
            i = k // m
        #print(i)
        #print(string[i])
        return string[i] + getPermutation(string[:i] + string[i+1:], k - i * m)
