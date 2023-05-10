def solve():
    a, b = map(int, input().split())
    if a == 0:
        print(0, 1)
    elif b == 0:
        print(1, 0)
    else:
        c = (b**2 / a**2 + 1) ** 0.5
        print(1 / (1 + c), c / (1 + c))

if __name__ == '__main__':
    solve()