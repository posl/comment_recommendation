def main():
    N = int(input())
    A = [0] * N
    X = [[] for _ in range(N)]
    Y = [[] for _ in range(N)]
    for i in range(N):
        A[i] = int(input())
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x - 1)
            Y[i].append(y)
    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(N):
            if i >> j & 1:
                for k in range(A[j]):
                    if i >> X[j][k] & 1 != Y[j][k]:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count("1"))
    print(ans)

if __name__ == '__main__':
    main()