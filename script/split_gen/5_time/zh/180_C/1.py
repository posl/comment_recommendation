def solve(n):
    ans = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
        i += 1
    ans.sort()
    return ans
