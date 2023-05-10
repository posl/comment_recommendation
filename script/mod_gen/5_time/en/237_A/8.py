def solve():
    N = int(input())
    if -2**31 <= N <= 2**31 - 1:
        print('Yes')
    else:
        print('No')
solve()

if __name__ == '__main__':
    solve()