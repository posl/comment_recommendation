def func(n, h):
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    return ans
