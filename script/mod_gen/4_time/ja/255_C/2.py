def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
        return
    if (x - a) % d == 0:
        if (x - a) // d < 0:
            print(1)
        else:
            print(0)
    else:
        if (x - a) // d < 0:
            print(2)
        else:
            print(1)

if __name__ == '__main__':
    main()