def main():
    A,B,C,D,E,F,X = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= X:
            print('Draw')
            break
        elif aoki >= X:
            print('Takahashi')
            break
        else:
            taka += A
            aoki += D
            if taka >= X:
                print('Takahashi')
                break
            elif aoki >= X:
