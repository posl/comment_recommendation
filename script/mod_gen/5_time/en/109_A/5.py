def solve():
    a,b = map(int, input().split())
    if a*b % 2 == 1:
        print('Yes')
    else:
        print('No')
solve()

if __name__ == '__main__':
    solve()