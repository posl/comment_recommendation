def solve(n,h):
    ans = 0
    for i in range(1,n+1):
        if h[i-1] == 0:
            continue
        else:
            ans += h[i-1]
            if i != n:
                if h[i] != 0:
                    ans += h[i-1]
    return ans
