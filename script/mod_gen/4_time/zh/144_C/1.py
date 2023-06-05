def solve(n):
    ans = 0
    while n > 1:
        if n % 2:
            n -= 1
        else:
            n //= 2
        ans += 1
    return ans

if __name__ == '__main__':
    solve()