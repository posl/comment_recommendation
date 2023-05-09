def main():
    N, M, Q = map(int, input().split())
    train = [0] * (N+1)
    for i in range(M):
        L, R = map(int, input().split())
        train[L-1] += 1
        train[R] -= 1
    for i in range(N):
        train[i+1] += train[i]
    for i in range(Q):
        p, q = map(int, input().split())
        print(train[q] - train[p-1])

if __name__ == '__main__':
    main()