def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    AB = []
    for i in range(N):
        A[i], B[i] = map(int, input().split())
        AB.append([A[i], B[i]])
    def dfs(i, x, y):
        if i == N:
            return float('inf')
        if x >= X and y >= Y:
            return 0
        res0 = dfs(i + 1, x, y)
        res1 = dfs(i + 1, x + AB[i][0], y + AB[i][1]) + 1
        return min(res0, res1)
    ans = dfs(0, 0, 0)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()