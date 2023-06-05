def solve():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ''
    while N != 0:
        r = N % (-2)
        N //= (-2)
        if r < 0:
            r += 2
            N += 1
        ans = str(r) + ans
    print(ans)

if __name__ == '__main__':
    solve()