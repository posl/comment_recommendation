def solve():
    N, M = map(int, input().split())
    
    def dfs(seq):
        if len(seq) == N:
            print(' '.join(map(str, seq)))
            return
        for i in range(seq[-1] + 1, M + 1):
            dfs(seq + [i])
    
    for i in range(1, M + 1):
        dfs([i])
solve()
