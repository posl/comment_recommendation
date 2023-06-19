def solve(n):
    from math import sqrt
    ans = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)
    return sorted(ans)
