def solve(a, n):
    if a == 1:
        return n - 1
    if a == n:
        return 1
    if a > n:
        return -1
    count = 0
    while n > 0:
        if n % a == 0:
            n //= a
        else:
            n -= 1
        count += 1
    return count

if __name__ == '__main__':
    solve()