def solve():
    x, y = map(int, input().split())
    if 2 * x <= y and y <= 4 * x and y % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()