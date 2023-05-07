def main():
    n = int(input())
    s = ''
    while n != 0:
        r = n % (-2)
        n = n // (-2)
        if r < 0:
            r += 2
            n += 1
        s = str(r) + s
    if s == '':
        s = '0'
    print(s)

if __name__ == '__main__':
    main()