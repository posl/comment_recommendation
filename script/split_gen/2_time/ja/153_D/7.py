def solve():
    h = int(input())
    ans = 0
    while h > 0:
        h = h // 2
        ans += 1 << ans
    print(ans)
