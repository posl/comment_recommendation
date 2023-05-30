def solve(n):
    s = ''
    while n > 0:
        if n % 2 == 0:
            n //= 2
            s = 'B' + s
        else:
            n -= 1
            s = 'A' + s
    return s
n = int(input())
print(solve(n))
