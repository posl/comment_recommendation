def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if n == 1:
            print(abs(x-a))
        else:
            diff = x - a
            if diff % d == 0:
                print(0)
            else:
                print(1)

if __name__ == '__main__':
    main()