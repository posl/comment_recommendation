def solve(a, n):
    if a == 1:
        return n - 1
    if a == n:
        return 1
    ans = 0
    while n > 0:
        if n % a == 0:
            n //= a
            ans += 1
        elif n % a != 1:
            return -1
        else:
            n -= 1
            ans += 1
    return ans

if __name__ == '__main__':
    solve()