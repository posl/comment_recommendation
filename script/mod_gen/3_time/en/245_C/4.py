def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n == 1:
        print('Yes')
        return
    if n == 2:
        if abs(a[0] - a[1]) <= k or abs(b[0] - b[1]) <= k or abs(a[0] - b[1]) <= k or abs(b[0] - a[1]) <= k:
            print('Yes')
        else:
            print('No')
        return
    for i in range(1, n - 1):
        if abs(a[i] - a[i + 1]) > k and abs(a[i] - b[i + 1]) > k and abs(b[i] - a[i + 1]) > k and abs(b[i] - b[i + 1]) > k:
            print('No')
            return
    print('Yes')
main()
