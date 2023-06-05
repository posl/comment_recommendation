def solve(n, k, p):
    #print(n, k, p)
    #print(p[0:k-1])
    #print(p[k-1:n])
    for i in range(k-1, n):
        print(sorted(p[0:i+1])[k-1])
    return 0
