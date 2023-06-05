def solve(n, a):
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 != 0 and a[i] % 5 != 0:
                return "DENIED"
    return "APPROVED"

if __name__ == '__main__':
    solve()