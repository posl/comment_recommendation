def main():
    N = int(input())
    path = [set() for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        path[a-1].add(b-1)
        path[b-1].add(a-1)
    def dfs(i, prev, ans):
        ans.append(i)
        for j in path[i]:
            if j != prev:
                dfs(j, i, ans)
        ans.append(i)
    ans = []
    dfs(0, -1, ans)
    print(*ans)
