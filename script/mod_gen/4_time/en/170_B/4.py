def solve():
    X, Y = map(int, input().split())
    if Y % 2 == 0 and 2 * X <= Y and Y <= 4 * X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()