def problem249_a():
    a,b,c,d,e,f,x = map(int,input().split())
    takahashi = 0
    aoki = 0
    while True:
        if takahashi + a <= x:
            takahashi += a
        else:
            takahashi = x
        if aoki + d <= x:
            aoki += d
        else:
            aoki = x
        if takahashi == aoki:
            print('Draw')
            break
        elif takahashi > aoki:

if __name__ == '__main__':
    problem249_a()