def solve():
    X = int(input())
    if X % 100 == 0 and X != 0:
        print('Yes')
    else:
        print('No')
    return 0

if __name__ == '__main__':
    solve()