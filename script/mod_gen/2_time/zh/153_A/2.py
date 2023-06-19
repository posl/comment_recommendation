def solve():
    H, A = map(int, input().split())
    print((H + A - 1) // A)
    return 0

if __name__ == '__main__':
    solve()