def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        return -1
    for i in range(1, n):
        if a[i] - a[i-1] != 1 and a[i] - a[i-1] != 0:
            return -1
    ans = 0
    for i in range(1, n):
        if a[i] - a[i-1] == 0:
            ans += 1
    return ans
