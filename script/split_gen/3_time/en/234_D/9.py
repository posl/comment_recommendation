def get_kth_greatest_value(n,k,p):
    p = p[:k] # p[0:k]
    p.sort(reverse=True)
    print(p[0])
    for i in range(k,n):
        if p[0] < p[i]:
            p[0] = p[i]
            p.sort(reverse=True)
        print(p[0])
