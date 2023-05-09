def main():
    a, b, x = map(int, input().split())
    if a * 10 ** 9 + b * 10 <= x:
        print(10 ** 9)
        return
    l = 0
    r = 10 ** 9
    while r - l > 1:
        m = (l + r) // 2
        if a * m + b * len(str(m)) <= x:
            l = m
        else:
            r = m
    print(l)

if __name__ == '__main__':
    main()