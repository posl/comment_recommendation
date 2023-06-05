def permutation(n, m, a, b, c, d):
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                for l in range(1,n+1):
                    if i==j or i==k or i==l or j==k or j==l or k==l:
                        continue
                    if (a[i] < a[j] and b[i] < b[j]) == (c[k] < c[l] and d[k] < d[l]):
                        continue
                    if (a[i] < a[j] and b[i] < b[j]) != (c[k] < c[l] and d[k] < d[l]):
                        return False
    return True
