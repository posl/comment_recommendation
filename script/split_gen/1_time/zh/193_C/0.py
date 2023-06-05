def solve(n):
    if n < 2:
        return 0
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        if i ** 2 > n:
            break
        j = 2
        while i ** j <= n:
            ans -= 1
            j += 1
    return ans
