def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l = max(a[0], b[0])
    r = min(a[0] + k, b[0] + k)
    for i in range(1, n):
        l = max(l, a[i], b[i])
        r = min(r, a[i] + k, b[i] + k)
        if l > r:
            print("No")
            return
    print("Yes")
