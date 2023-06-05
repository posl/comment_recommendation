def solve(N, cs):
    ans = 0
    for i in range(N):
        if cs[i] == "W":
            ans += 1
    if ans == 0:
        return 0
    elif ans == N:
        return N
    else:
        r = 0
        w = ans
        for i in range(N):
            if cs[i] == "R":
                r += 1
            else:
                w -= 1
            ans = min(ans, max(r, w))
        return ans

if __name__ == '__main__':
    solve()