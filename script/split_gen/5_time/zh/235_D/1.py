def solve(a, n):
    if a % 2 == 0:
        return solve(a // 2, n) + 1
    elif a % 5 == 0:
        return solve(a // 5, n) + 1
    elif a == 1:
        return 0
    else:
        x = 1
        for i in range(1, n + 1):
            x = (10 * x) % a
            if x == 1:
                return i
        return -1
a, n = map(int, input().split())
print(solve(a, n))
