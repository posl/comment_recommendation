def main():
    n, d = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(n)]
    lrs.sort()
    ans = 0
    r = 0
    for i in range(n):
        if r < lrs[i][0]:
            r = lrs[i][0]
        if r + d <= lrs[i][1]:
            ans += 1
            r += d
    print(ans)
main()
