def main():
    a,b,c,d,e,f,x = map(int, input().split())
    taka = 0
    aoki = 0
    while x > 0:
        if a > x:
            taka += x
            x = 0
        else:
            taka += a
            x -= a
            if c > x:
                x = 0
            else:
                x -= c
        if d > x:
            aoki += x
            x = 0
        else:
            aoki += d
            x -= d
            if f > x:
                x = 0
            else:
                x -= f
    if taka > aoki:
        print('高桥')
    elif taka < aoki:
        print('青木')
    else:
        print('画')

if __name__ == '__main__':
    main()