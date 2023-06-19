def solve(n, c):
    if n == 1:
        return 1 if c == 'W' else 0
    if n == 2:
        return 1 if c == 'R' else 0
    cnt = 0
    if c == 'W':
        cnt += 1
    for i in range(1, n):
        if c == 'R':
            if i % 2 == 0:
                cnt += 1
        else:
            if i % 2 == 1:
                cnt += 1
    return cnt
