def solve(n, a):
    b = [0] * (n + 1)
    for i in range(4 * n - 1):
        b[a[i]] += 1
    for i in range(1, n + 1):
        if b[i] % 2 == 1:
            return i
n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
