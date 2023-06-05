def check():
    n,m = map(int,input().split())
    l = []
    r = []
    for i in range(m):
        l1,r1 = map(int,input().split())
        l.append(l1)
        r.append(r1)
    l.sort()
    r.sort()
    # print(l)
    # print(r)
    if l[-1] > r[0]:
        return 0
    else:
        return r[0]-l[-1]+1
print(check())
