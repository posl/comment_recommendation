def solve():
    n, a, b = map(int, input().split())
    s = input()
    if n % 2 == 0:
        print(min(a * n, b * (n // 2)))
    else:
        print(min(a * n, b * (n // 2) + a))

if __name__ == '__main__':
    solve()