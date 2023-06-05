def main():
    a, b, c, d, e, f, x = map(int, input().split())
    t = 0
    while x > 0:
        if a > 0:
            x -= b
            t += a
        if x <= 0:
            break
        x -= c
        if x <= 0:
            break
        if d > 0:
            x -= e
            t -= d
        if x <= 0:
            break
        x -= f
    if t < 0:
        print("青木")
    elif t > 0:
        print("高桥")
    else:
        print("画")

if __name__ == '__main__':
    main()