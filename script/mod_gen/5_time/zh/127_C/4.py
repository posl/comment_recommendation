def problems127_c():
    n,m = map(int,input().split())
    l = []
    r = []
    for i in range(m):
        l1,r1 = map(int,input().split())
        l.append(l1)
        r.append(r1)
    print(max(0,min(r)-max(l)+1))

if __name__ == '__main__':
    problems127_c()