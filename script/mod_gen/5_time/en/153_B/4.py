def solve():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    print('Yes' if sum(a) >= h else 'No')

if __name__ == '__main__':
    solve()