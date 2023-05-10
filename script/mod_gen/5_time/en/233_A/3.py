def solve(x, y):
    cnt = 0
    while True:
        x += 10
        cnt += 1
        if x >= y:
            break
    return cnt

if __name__ == '__main__':
    solve()