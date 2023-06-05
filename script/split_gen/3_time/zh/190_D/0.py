def solve(n):
    if n == 1:
        return 2
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if i%2 == 1 and n%i == 0:
            ans += 2
        elif i%2 == 0 and n%i == i//2:
            ans += 1
    return ans
