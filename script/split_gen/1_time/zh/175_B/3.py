def triangles(l):
    l.sort()
    n = len(l)
    cnt = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i] != l[j] and l[j] != l[k] and l[i] + l[j] > l[k]:
                    cnt += 1
    return cnt
