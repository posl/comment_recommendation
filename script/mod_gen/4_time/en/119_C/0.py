def dfs(i, a, b, c):
    if i == N:
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return float('inf')
    res0 = dfs(i + 1, a, b, c)
    res1 = dfs(i + 1, a + L[i], b, c) + 10
    res2 = dfs(i + 1, a, b + L[i], c) + 10
    res3 = dfs(i + 1, a, b, c + L[i]) + 10
    return min(res0, res1, res2, res3)
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

if __name__ == '__main__':
    dfs()