def main():
    a,b,c,d,e,f,x = map(int,input().split())
    t = 0
    while True:
        if t >= x:
            print('Draw')
            return
        t += 1
        if t % (a+c) <= a and t % (d+f) <= d:
            print('Draw')
            return
        elif t % (a+c) <= a:
            print('Takahashi')
            return
        elif t % (d+f) <= d:
            print('Aoki')
            return
main()

if __name__ == '__main__':
    main()