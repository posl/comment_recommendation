def solve(N):
    res = []
    while N > 0:
        if N % 2 == 1:
            res.append('A')
            N -= 1
        else:
            res.append('B')
            N //= 2
    res.reverse()
    return "".join(res)

if __name__ == '__main__':
    solve()