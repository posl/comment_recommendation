def solve(N, M, AB):
    ans = [-1] * N
    for i in range(M):
        a = AB[i][0]
        b = AB[i][1]
        if ans[a-1] == -1 and ans[b-1] == -1:
            ans[a-1] = b
            ans[b-1] = a
        elif ans[a-1] == -1:
            ans[a-1] = b
        elif ans[b-1] == -1:
            ans[b-1] = a
        else:
            if ans[a-1] != b or ans[b-1] != a:
                return [-1]
    return ans
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
ans = solve(N, M, AB)
