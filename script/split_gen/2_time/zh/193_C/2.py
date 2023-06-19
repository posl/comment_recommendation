def solve(n):
    num = 0
    for i in range(2, int(n**0.5)+1):
        x = i
        while x <= n:
            x *= i
            num += 1
    return n - num
