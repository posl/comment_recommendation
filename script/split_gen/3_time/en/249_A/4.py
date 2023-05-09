def main():
    a,b,c,d,e,f,x = map(int, input().split())
    t = 0
    aoki = 0
    takahashi = 0
    while t < x:
        takahashi += a
        t += b
        if t >= x:
            break
        t += c
        aoki += d
        if t >= x:
            break
        t += e
        takahashi += f
    if takahashi > aoki:
        print('Takahashi')
    elif aoki > takahashi:
        print('Aoki')
    else:
        print('Draw')
