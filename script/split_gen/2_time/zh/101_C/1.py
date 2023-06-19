def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    min_a = min(a)
    count = 0
    for i in range(n):
        if a[i] == min_a:
            count += 1
    if (count - k) % (k - 1) == 0:
        print((count - k) // (k - 1) + 1)
    else:
        print((count - k) // (k - 1) + 2)
solve()
