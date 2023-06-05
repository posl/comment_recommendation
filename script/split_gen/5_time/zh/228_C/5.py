def is_top_k(n, k, p):
    #p.sort(key=lambda x:x[0]+x[1]+x[2], reverse=True)
    p.sort(reverse=True)
    #print(p)
    for i in range(n):
        if i < k:
            if p[i][0]+p[i][1]+p[i][2] < p[k-1][0]+p[k-1][1]+p[k-1][2]:
                return 'No'
    return 'Yes'
