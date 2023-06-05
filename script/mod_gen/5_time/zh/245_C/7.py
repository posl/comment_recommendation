def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(1, n):
        if abs(a[i] - a[i-1]) > k and abs(b[i] - b[i-1]) > k:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    solve()