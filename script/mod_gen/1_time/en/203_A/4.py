def solve():
    a, b, c = map(int, input().split())
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return 0
print(solve())

if __name__ == '__main__':
    solve()