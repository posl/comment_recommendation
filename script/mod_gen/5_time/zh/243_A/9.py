def main():
    v,a,b,c = map(int, input().split())
    while True:
        if v >= a:
            v -= a
        else:
            print('F')
            break
        if v >= b:
            v -= b
        else:
            print('M')
            break
        if v >= c:
            v -= c
        else:
            print('T')
            break

if __name__ == '__main__':
    main()