def solve(n):
    s = str(n)
    l = len(s)
    cnt = 0
    for i in range(3, l+1, 3):
        cnt += (l-i+1) * 10**(i//3-1)
    cnt += (n - 10**(l-1) + 1) * (l//3)
    return cnt

if __name__ == '__main__':
    solve()