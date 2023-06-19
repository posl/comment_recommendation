def main():
    n, m, q = map(int, input().split())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    ans = 0
    def dfs(A):
        nonlocal ans
        if len(A) == n:
            s = 0
            for i in range(q):
                if A[query[i][1]-1] - A[query[i][0]-1] == query[i][2]:
                    s += query[i][3]
            ans = max(ans, s)
            return
        for i in range(A[-1], m+1):
            dfs(A+[i])
    for i in range(1, m+1):
        dfs([i])
    print(ans)
