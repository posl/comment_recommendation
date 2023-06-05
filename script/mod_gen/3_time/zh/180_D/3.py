def problems180_d():
    x, y, a, b = map(int, input().split())
    cnt = 0
    while x*a < x+b and x*a < y:
        x *= a
        cnt += 1
    print(cnt + (y-1-x)//b)

if __name__ == '__main__':
    problems180_d()