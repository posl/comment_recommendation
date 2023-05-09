def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    X = [[0] * N for _ in range(N)]
    Y = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(A[i]):
            x, y = map(int, input().split())
            X[i][x - 1] = y
            Y[i][j] = x - 1
    ans = 0
    for i in range(2 ** N):
        cnt = 0
        for j in range(N):
            if (i >> j) & 1:
                cnt += 1
                for k in range(A[j]):
                    if X[j][Y[j][k]] == 0:
                        cnt = 0
                        break
                    elif X[j][Y[j][k]] == 1 and ((i >> Y[j][k]) & 1) == 0:
                        cnt = 0
                        break
        ans = max(ans, cnt)
    print(ans)
solve()
The key to this problem is that the number of testimonies given by an honest person is equal to the number of honest persons. Therefore, we can check all the possible combinations of the number of honest persons and the number of testimonies given by each person. The following code solves this problem by brute force.

if __name__ == '__main__':
    solve()