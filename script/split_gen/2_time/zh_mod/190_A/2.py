def main():
    a,b,c = map(int,input().split())
    if c == 0:
        if a > b:
            print('Takahashi')
        else:
            print('Aoki')
    elif c == 1:
        if a < b:
            print('Aoki')
        else:
            print('Takahashi')
