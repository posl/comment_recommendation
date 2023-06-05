def solve(n, a):
    if a[0] > 1:
        return 0
    if a[0] == 1:
        for i in range(1, n):
            if a[i] > i + 1:
                return i
        return n
    if a[0] == 0:
        return 1
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
