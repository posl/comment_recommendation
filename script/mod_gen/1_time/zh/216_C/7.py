def solve(n):
    res = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            res.append('B')
        else:
            n = n - 1
            res.append('A')
    return ''.join(res[::-1])
n = int(input())
print(solve(n))
