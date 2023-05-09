def main():
    n, m, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')
    for i in range(2**n):
        b = [0] * m
        cost = 0
        for j in range(n):
            if i >> j & 1:
                cost += a[j][0]
                for k in range(m):
                    b[k] += a[j][k+1]
        if min(b) >= x:
            ans = min(ans, cost)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
