def main():
    N,M,Q = map(int, input().split())
    train = []
    for i in range(M):
        L,R = map(int, input().split())
        train.append([L,R])
    for i in range(Q):
        p,q = map(int, input().split())
        count = 0
        for j in range(M):
            if train[j][0] >= p and train[j][1] <= q:
                count += 1
        print(count)

if __name__ == '__main__':
    main()