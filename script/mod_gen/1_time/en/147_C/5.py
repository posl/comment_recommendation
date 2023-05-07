def solve():
    # write your code here
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = []
    Y = []
    for i in range(N):
        x = []
        y = []
        for _ in range(A[i]):
            _x, _y = map(int, input().split())
            x.append(_x)
            y.append(_y)
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(2 ** N):
        ok = True
        for j in range(N):
            if (i >> j) & 1:
                for k in range(A[j]):
                    if ((i >> (X[j][k] - 1)) & 1) != Y[j][k]:
                        ok = False
                        break
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)
solve()

if __name__ == '__main__':
    solve()