def solve():
    n, c = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(n)]
    # 1. 每天都订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    print(ans)
    # 2. 从第 2 天开始订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    min_c = min(c for a, b, c in abc)
    ans += min_c * (n - 1)
    print(ans)
    # 3. 从第 2 天开始订阅，并且在第 1 天取消订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    min_c = min(c for a, b, c in abc)
    ans += min_c * (n - 1)
    ans += min(c for a, b, c in abc if a == 1)
    print(ans)
    # 4. 从第 2 天开始订阅，并且在最后一天取消订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    min_c = min(c for a, b, c in abc)
    ans += min_c * (n - 1)
    ans += min(c for a, b, c in abc if b == 10 ** 9)
    print(ans)
    # 5. 从第 2 天开始订阅，并且在第 1 天和最后一天取消订阅
    ans = 0
    for a, b, c in abc:
        ans += c * (b - a + 1)
    min_c = min(c for a, b, c in abc)
    ans += min_c * (n - 1)
    ans += min(c for a, b, c in abc if a == 1)
    ans += min(c for

if __name__ == '__main__':
    solve()