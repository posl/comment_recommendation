def f(n):
    ans = 0
    for i in range(1, n+1):
        ans += i * (n // i)
    return ans
n = int(input())
print(f(n))
