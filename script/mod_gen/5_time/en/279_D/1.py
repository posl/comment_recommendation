def solve():
    A, B = map(int, input().split())
    if B == 1:
        print(A)
    else:
        print((A - 1) / (B - 1))
solve()

if __name__ == '__main__':
    solve()