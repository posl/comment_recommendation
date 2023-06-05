def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in range(m):
        b1,c1 = map(int,input().split())
        b.append(b1)
        c.append(c1)
    b = [b[i] for i in range(m) if c[i] > a[b[i]-1]]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            b[i+1] += 1
    b = [b[i] for i in range(len(b)) if b[i] <= n]
    b.sort()
    for i in range(len(b)-1):
        if b[i] == b[i+

if __name__ == '__main__':
    solve()