def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if d > 0:
        if x < a:
            print(1)
        else:
            print((x - a) // d + 1)
        return
    if d < 0:
        if x > a:
            print(1)
        else:
            print((a - x) // (-d) + 1)
        return
    print(0)
    return

if __name__ == '__main__':
    main()