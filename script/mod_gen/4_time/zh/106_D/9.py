def main():
    n,m,q = map(int,input().split())
    L = [0] * m
    R = [0] * m
    p = [0] * q
    q = [0] * q
    for i in range(m):
        L[i],R[i] = map(int,input().split())
    for i in range(q):
        p[i],q[i] = map(int,input().split())
    for i in range(q):
        count = 0
        for j in range(m):
            if p[i] <= L[j] and R[j] <= q[i]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()