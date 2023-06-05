def exchange(a,p,q,r,s):
    b = a.copy()
    for i in range(q-p+1):
        b[p+i-1] = a[s+i-1]
        b[s+i-1] = a[p+i-1]
    return b

if __name__ == '__main__':
    exchange()