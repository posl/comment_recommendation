def main():
    n, m = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(8):
        s = [0] * n
        for j in range(n):
            for k in range(3):
                if (i >> k) & 1:
                    s[j] += cakes[j][k]
                else:
                    s[j] -= cakes[j][k]
        s.sort(reverse=True)
        ans = max(ans, sum(s[:m]))
    print(ans)
