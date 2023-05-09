def dfs(i, a, b, c):
    if i == N:
        return abs(a - A) + abs(b - B) + abs(c - C) if min(a, b, c) > 0 else float('inf')
    res0 = dfs(i + 1, a, b, c)
    res1 = dfs(i + 1, a + L[i], b, c) + 10 if a else float('inf')
    res2 = dfs(i + 1, a, b + L[i], c) + 10 if b else float('inf')
    res3 = dfs(i + 1, a, b, c + L[i]) + 10 if c else float('inf')
    return min(res0, res1, res2, res3)
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

if __name__ == '__main__':
    dfs()