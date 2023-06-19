def get_max_score(n, m, q, abcd):
    def dfs(a, start):
        if len(a) == n:
            score = 0
            for b, c, d in abcd:
                if a[b-1] - a[a-1] == c:
                    score += d
            return score
        else:
            ans = 0
            for i in range(start, m+1):
                ans = max(ans, dfs(a + [i], i))
            return ans
    return dfs([], 1)
n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]
print(get_max_score(n, m, q, abcd))
