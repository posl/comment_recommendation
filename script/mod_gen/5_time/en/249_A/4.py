def main():
    a,b,c,d,e,f,x = map(int,input().split())
    takahashi = 0
    aoki = 0
    for i in range(x):
        if i % (a + b) < a:
            takahashi += c
        if i % (d + e) < d:
            aoki += f
    if takahashi > aoki:
        print('Takahashi')
    elif takahashi < aoki:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()