def f(n):
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    return ans
n = int(input())
print(f(n))
