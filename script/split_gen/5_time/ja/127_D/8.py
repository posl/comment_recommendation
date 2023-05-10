def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = []
    c = []
    for i in range(m):
        b_,c_ = map(int, input().split())
        b.append(b_)
        c.append(c_)
    d = []
    for i in range(n):
        d.append(a[i])
    for i in range(m):
        for j in range(b[i]):
            if c[i] > d[-1]:
                d.pop()
            else:
                break
        for j in range(b[i]):
            d.append(c[i])
    print(sum(d))
