def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    if 2 * x < y or 2 * y < x:
        print(0)
        return
    n = (2 * x - y) // 3
    m = (2 * y - x) // 3
    ans = 1
    mod = 10 ** 9 + 7
    for i in range(1, n + 1):
        ans = (ans * (m + i)) % mod
        ans = (ans * pow(i, mod - 2, mod)) % mod
    print(ans)
