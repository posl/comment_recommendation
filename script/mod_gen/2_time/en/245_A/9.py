def problems245_a():
    a,b,c,d = map(int, input().split())
    if a*60+b < c*60+d:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    problems245_a()