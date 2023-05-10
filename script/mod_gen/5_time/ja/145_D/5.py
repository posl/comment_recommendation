def main():
    X,Y = map(int, input().split())
    if (X+Y)%3 != 0:
        print(0)
        return
    if X*2 < Y or X > Y*2:
        print(0)
        return
    if X == Y:
        print(2**X % (10**9+7))
        return
    else:
        if X < Y:
            X,Y = Y,X
        n = (X+Y)//3
        r = X-n
        a = 1
        b = 1
        for i in range(r):
            a = a * (n-i) % (10**9+7)
            b = b * (i+1) % (10**9+7)
        b = pow(b, 10**9+5, 10**9+7)
        print(a*b % (10**9+7))
        return

if __name__ == '__main__':
    main()