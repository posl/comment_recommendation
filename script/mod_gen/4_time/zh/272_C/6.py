def solve(n, a):
    a.sort()
    for i in range(n - 1, 0, -1):
        if a[i] == a[i - 1]:
            return a[i] * 2
    return -1
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
