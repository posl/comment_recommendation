def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    a.append(t)
    b.append(t)
    charge = 0
    for i in range(m+1):
        charge += a[i] - b[i-1]
        if charge > n:
            charge = n
        if charge <= 0:
            print('No')
            break
    else:
        print('Yes')
