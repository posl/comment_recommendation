def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    ta = 0
    ao = 0
    while True:
        if t >= x:
            break
        ta += a
        t += 1
        if t >= x:
            break
        ao += d
        t += 1
    if ta > ao:
        print('Takahashi')
    elif ta < ao:
        print('Aoki')
    else

if __name__ == '__main__':
    main()