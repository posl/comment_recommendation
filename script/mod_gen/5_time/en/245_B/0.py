def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        return 0
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            return a[i-1] + 1
    return a[n-1] + 1
print(solve())
