def triangle(n, l):
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i]+l[j] > l[k] and l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    ans += 1
    return ans
