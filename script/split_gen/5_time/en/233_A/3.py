def solve(x, y):
    cnt = 0
    while True:
        x += 10
        cnt += 1
        if x >= y:
            break
    return cnt
