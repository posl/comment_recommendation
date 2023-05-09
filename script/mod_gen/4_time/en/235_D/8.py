def solve(a, n):
    if n < 10:
        if n == a:
            return 1
        else:
            return -1
    else:
        s = str(n)
        if s[-1] == '0':
            return solve(a, int(s[:-1]))
        else:
            x = int(s[-1] + s[:-1])
            y = solve(a, x)
            if y > 0:
                return y + 1
            else:
                z = solve(a, n * a)
                if z > 0:
                    return z + 1
                else:
                    return -1
a, n = [int(x) for x in input().split()]
print(solve(a, n))

if __name__ == '__main__':
    solve()