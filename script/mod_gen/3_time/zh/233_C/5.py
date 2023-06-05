def solve():
    N, X = map(int, input().split())
    bag = []
    for i in range(N):
        bag.append(list(map(int, input().split()))[1:])
    def dfs(i, X):
        if i == N:
            return 1 if X == 1 else 0
        res = 0
        for j in range(len(bag[i])):
            if X % bag[i][j] == 0:
                res += dfs(i + 1, X // bag[i][j])
        return res
    print(dfs(0, X))
solve()
