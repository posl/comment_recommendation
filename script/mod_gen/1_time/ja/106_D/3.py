def main():
    n,m,q = map(int,input().split())
    l = [0] * m
    r = [0] * m
    p = [0] * q
    q = [0] * q
    for i in range(m):
        l[i],r[i] = map(int,input().split())
    for i in range(q):
        p[i],q[i] = map(int,input().split())
    for i in range(q):
        cnt = 0
        for j in range(m):
            if p[i] <= l[j] and r[j] <= q[i]:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()