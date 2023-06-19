def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # 1~n
    # 1~k
    # 1~n
    # 1~n
    # 1~k
    # 1~n
    for i in range(k):
        a[b[i]-1] = 0
    print('Yes' if max(a) > 0 else 'No')

if __name__ == '__main__':
    solve()