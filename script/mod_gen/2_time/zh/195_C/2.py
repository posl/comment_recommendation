def solve(n):
    ans = 0
    for i in range(1, len(str(n))+1):
        if i % 3 == 0:
            continue
        ans += 9 * 10 ** (i-1) * i
    ans += (n - 10 ** (len(str(n))-1) + 1) * len(str(n))
    return ans

if __name__ == '__main__':
    solve()