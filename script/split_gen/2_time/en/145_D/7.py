def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    x, y = sorted([x, y])
    n = (x + y) // 3
    m = min(x, y) - n
    ans = 1
    for i in range(n + 1, n + m + 1):
        ans = ans * i % (10**9 + 7)
    for i in range(1, m + 1):
        ans = ans * pow(i, -1, 10**9 + 7) % (10**9 + 7)
    print(ans)
