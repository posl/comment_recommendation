def solve(n):
    ans = ''
    while n > 0:
        if n % 2 == 0:
            n //= 2
            ans += 'B'
        else:
            n -= 1
            ans += 'A'
    return ans[::-1]

if __name__ == '__main__':
    solve()