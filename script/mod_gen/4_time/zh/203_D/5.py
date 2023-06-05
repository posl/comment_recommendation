def median(m, n, k, arr):
    #print(m, n, k, arr)
    s = []
    for i in range(m-k+1):
        for j in range(n-k+1):
            #print(i, j)
            t = []
            for x in range(k):
                for y in range(k):
                    t.append(arr[i+x][j+y])
            t.sort()
            #print(t)
            s.append(t[(k*k//2)+1])
    s.sort()
    #print(s)
    return s[0]

if __name__ == '__main__':
    median()