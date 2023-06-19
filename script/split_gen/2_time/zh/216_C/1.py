def solve(n):
    ans = ''
    while n > 0:
        if n % 2 == 0:
            ans += 'B'
            n //= 2
        else:
            ans += 'A'
            n -= 1
    return ans[::-1]
n = int(input())
print(solve(n))
