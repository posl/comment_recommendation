def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    x = [[None for _ in range(A[i])] for i in range(N)]
    y = [[None for _ in range(A[i])] for i in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x[i][j], y[i][j] = map(int, input().split())
    ans = 0
    for i in range(1 << N):
        ok = True
        for j in range(N):
            if i >> j & 1:
                for k in range(A[j]):
                    if y[j][k] == 1 and i >> (x[j][k] - 1) & 1 == 0:
                        ok = False
        if ok:
            ans = max(ans, bin(i).count('1'))
    print(ans)

if __name__ == '__main__':
    solve()