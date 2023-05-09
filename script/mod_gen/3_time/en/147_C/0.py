def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[] for _ in range(N)]
    Y = [[] for _ in range(N)]
    for i in range(N):
        for _ in range(A[i]):
            x, y = map(int, input().split())
            X[i].append(x - 1)
            Y[i].append(y)
    ans = 0
    for bit in range(1 << N):
        flag = True
        for i in range(N):
            if bit & (1 << i):
                for x, y in zip(X[i], Y[i]):
                    if y == 0 and bit & (1 << x):
                        flag = False
                    if y == 1 and not bit & (1 << x):
                        flag = False
        if flag:
            ans = max(ans, bin(bit).count("1"))
    print(ans)

if __name__ == '__main__':
    main()