def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    a.insert(0,0)
    b.insert(0,0)
    a.append(t)
    b.append(t)
    #print(a)
    #print(b)
    for i in range(m+1):
        if i == 0:
            if a[i] > 0:
                n -= a[i]
                if n <= 0:
                    print('No')
                    return
        else:
            if a[i] - b[i-1] > 0:
                n -= a[i] - b[i-1]
                if n <= 0:
                    print('No')
                    return
            else:
                pass
        n += b[i] - a[i]
        if n > 10**9:
            n = 10**9
    if n > 0:
        print('Yes')
    else:
        print('No')
