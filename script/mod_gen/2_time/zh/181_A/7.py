def solve(x,y,a,b):
    cnt = 0
    while True:
        if x * a < x + b:
            x *= a
            cnt += 1
        else:
            break
    cnt += (y - x - 1) // b
    return cnt

if __name__ == '__main__':
    solve()