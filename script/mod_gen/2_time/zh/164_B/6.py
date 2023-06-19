def main():
    a,b,c,d = map(int, input().split())
    while a > 0 and c > 0:
        c -= b
        if c <= 0:
            print('是')
            return
        a -= d
        if a <= 0:
            print('否')
            return

if __name__ == '__main__':
    main()