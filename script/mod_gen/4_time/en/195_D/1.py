def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X_copy = X.copy()
        del X_copy[L-1:R]
        X_copy.sort()
        baggages = []
        for x in X_copy:
            baggages.append((x, -1))
        for i in range(N):
            baggages.append((W[i], V[i]))
        baggages.sort(reverse=True)
        used = [False] * N
        ans = 0
        for x, v in baggages:
            for i in range(N):
                if not used[i] and W[i] <= x:
                    used[i] = True
                    ans += v
                    break
        print(ans)

if __name__ == '__main__':
    main()