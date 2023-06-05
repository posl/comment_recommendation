def main():
    a,b,c,d,e,f,x = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= x and aoki >= x:
            print('DRAW')
            break
        taka += a
        aoki += d
        if taka >= x and aoki >= x:
            print('DRAW')
            break
        aoki += e
        if taka >= x and aoki >= x:
            print('DRAW')
            break
        taka += b
        if taka >= x and aoki >= x:
            print('DRAW')
            break
        if taka > aoki:
            print('TAKAHASHI')
            break
        elif taka < aoki:
            print('AOKI')
            break
