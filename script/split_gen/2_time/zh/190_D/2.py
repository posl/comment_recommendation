def solve(n):
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0 and n // i % 2 == 1:
                ans += 1
            if i % 2 == 1 and n // i % 2 == 0:
                ans += 1
    return ans * 2
n = int(input())
print(solve(n))
