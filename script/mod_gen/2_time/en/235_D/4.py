def solve(a, n):
    if n == 1:
        return 0
    if a == 1:
        return -1
    cnt = 0
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            n -= 1
        cnt += 1
    return cnt
a, n = map(int, input().split())
print(solve(a, n))

if __name__ == '__main__':
    solve()