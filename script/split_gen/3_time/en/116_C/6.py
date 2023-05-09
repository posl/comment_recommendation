def solve(N, h):
    count = 0
    while True:
        if max(h) == 0:
            break
        l = 0
        r = 0
        for i in range(N):
            if h[i] > 0:
                l = i
                break
        for i in range(l, N):
            if h[i] == 0:
                r = i - 1
                break
            elif i == N - 1:
                r = i
        for i in range(l, r + 1):
            h[i] -= 1
        count += 1
    return count
