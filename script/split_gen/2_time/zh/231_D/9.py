def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    a = sorted(a)
    b = sorted(b)
    if a[0] > b[-1]:
        print('No')
    else:
        print('Yes')
