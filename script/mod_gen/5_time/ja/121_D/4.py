def solve():
    a, b = map(int, input().split())
    if a == b:
        return a
    if a % 2 == 0:
        if (b - a) % 4 == 0:
            return b
        else:
            return b ^ 1
    else:
        if (b - a) % 4 == 0:
            return b ^ a ^ 1
        else:
            return b ^ a
print(solve())

if __name__ == '__main__':
    solve()