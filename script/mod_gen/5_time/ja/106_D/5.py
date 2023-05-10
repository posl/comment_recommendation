def main():
    N,M,Q = map(int,input().split())
    train = []
    for i in range(M):
        L,R = map(int,input().split())
        train.append([L,R])
    train.sort()
    for i in range(Q):
        p,q = map(int,input().split())
        ans = 0
        for j in range(M):
            if p <= train[j][0] and train[j][1] <= q:
                ans += 1
        print(ans)

if __name__ == '__main__':
    main()