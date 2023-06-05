def solve(n):
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        j = 2
        while i ** j <= n:
            ans -= 1
            j += 1
    return ans
n = int(input())
print(solve(n))
