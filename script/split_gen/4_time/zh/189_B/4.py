def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        a,b = map(int,input().split())
        v.append(a)
        p.append(b)
    s = 0
    for i in range(n):
        s += v[i]*p[i]
        if s > x*100:
            print(i+1)
            return
    print(-1)
    return
