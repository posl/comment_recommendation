def main():
    a, b, c, d, e, f, x = map(int, input().split())
    h = 0
    q = 0
    for i in range(x):
        if i % (a + b) < a:
            h += 1
        if i % (d + e) < d:
            q += 1
    if h > q:
        print("高桥")
    elif h < q:
        print("青木")
    else:
        print("画")

if __name__ == '__main__':
    main()