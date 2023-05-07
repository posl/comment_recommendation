def dfs(i, a, b, c):
    if i == n:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a,b,c) > 0 else float('inf')
    ret0 = dfs(i+1, a, b, c)
    ret1 = dfs(i+1, a+l[i], b, c) + 10 if a else float('inf')
    ret2 = dfs(i+1, a, b+l[i], c) + 10 if b else float('inf')
    ret3 = dfs(i+1, a, b, c+l[i]) + 10 if c else float('inf')
    ret4 = dfs(i+1, a, b, c) + min(l[i], 10)
    return min(ret0, ret1, ret2, ret3, ret4)
n, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(n)]
print(dfs(0,0,0,0))

if __name__ == '__main__':
    dfs()