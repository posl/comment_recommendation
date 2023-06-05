def solve(n, m, sc):
    for i in range(10 ** (n - 1), 10 ** n):
        s = str(i)
        for j in range(m):
            if s[sc[j][0] - 1] != str(sc[j][1]):
                break
        else:
            return i
    return -1

if __name__ == '__main__':
    solve()