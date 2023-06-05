def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (2 * Y - X) // 3
    m = (2 * X - Y) // 3
    if n < 0 or m < 0:
        print(0)
        return
    ans = 1
    for i in range(n):
        ans = ans * (n + m - i) % (10 ** 9 + 7)
        ans = ans * pow(i + 1, 10 ** 9 + 5, 10 ** 9 + 7) % (10 ** 9 + 7)
    print(ans)
main()
