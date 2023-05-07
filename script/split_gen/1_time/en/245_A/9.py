def main():
    A,B,C,D = map(int,input().split())
    if A>B:
        print('Takahashi')
    elif A==B:
        if C>D:
            print('Takahashi')
        elif C==D:
            print('Draw')
        else:
            print('Aoki')
    else:
        print('Aoki')
