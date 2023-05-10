def main():
    n,m,q = map(int,input().split())
    l = [0]*m
    r = [0]*m
    for i in range(m):
        l[i],r[i] = map(int,input().split())
    p = [0]*q
    q = [0]*q
    for i in range(q):
        p[i],q[i] = map(int,input().split())

if __name__ == '__main__':
    main()