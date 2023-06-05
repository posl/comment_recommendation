def main():
    x = int(input())
    m = int(input())
    x = str(x)
    d = 0
    for i in x:
        if int(i) > d:
            d = int(i)
    n = d + 1
    while True:
        if int(x, n) > m:
            n -= 1
            break
        n += 1
    print(n - d)

if __name__ == '__main__':
    main()