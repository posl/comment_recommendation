def solve():
    h,n = map(int, input().split())
    a = list(map(int, input().split()))
    print('Yes' if h <= sum(a) else 'No')

if __name__ == '__main__':
    solve()