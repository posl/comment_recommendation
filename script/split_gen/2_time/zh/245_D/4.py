def solve(n, k, a, b):
    res = True
    for i in range(n):
        if abs(a[i] - b[i]) > k:
            res = False
            break
    return "Yes" if res else "No"
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, k, a, b))
