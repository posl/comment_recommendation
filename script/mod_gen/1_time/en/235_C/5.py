def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i] = A[i]
        Y[i] = i + 1
    for _ in range(Q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(N):
            if X[i] == x:
                cnt += 1
                if cnt == k:
                    print(Y[i])
                    break
        else:
            print(-1)

if __name__ == '__main__':
    main()