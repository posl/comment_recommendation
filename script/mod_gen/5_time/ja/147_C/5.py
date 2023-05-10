def solve():
    N = int(input())
    A = []
    X = []
    Y = []
    for i in range(N):
        a = int(input())
        A.append(a)
        x = []
        y = []
        for j in range(a):
            _x, _y = map(int, input().split())
            x.append(_x)
            y.append(_y)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if i & (1 << j):
                for k in range(A[j]):
                    if Y[j][k] == 1 and not i & (1 << (X[j][k] - 1)):
                        ok = False
                    if Y[j][k] == 0 and i & (1 << (X[j][k] - 1)):
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)

if __name__ == '__main__':
    solve()