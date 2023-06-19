def problems180_d():
    x, y, a, b = map(int, input().split())
    exp = 0
    while True:
        if x * a <= x + b and x * a < y:
            x *= a
            exp += 1
        else:
            if x + b < y:
                x += b
                exp += 1
            else:
                break
    print(exp)

if __name__ == '__main__':
    problems180_d()