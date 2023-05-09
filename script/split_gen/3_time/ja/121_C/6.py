def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    for i in range(n):
        if m == 0:
            break
        if ab[i][1] >= m:
            ans += ab[i][0] * m
            m = 0
        else:
            ans += ab[i][0] * ab[i][1]
            m -= ab[i][1]
    print(ans)
