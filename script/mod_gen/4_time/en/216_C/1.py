def solve(n):
    s = ''
    while n > 0:
        if n % 2 == 0:
            s = 'B' + s
            n //= 2
        else:
            s = 'A' + s
            n -= 1
    return s
n = int(input())
print(solve(n))

if __name__ == '__main__':
    solve()