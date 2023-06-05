def solve(a, l, r, x):
    cnt = 0
    for i in range(l-1, r):
        if a[i] == x:
            cnt += 1
    return cnt
