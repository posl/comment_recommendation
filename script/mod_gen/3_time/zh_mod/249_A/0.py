def main():
    #输入
    A,B,C,D,E,F,X = map(int,input().split())
    #计算
    #高桥
    Takahashi = 0
    Takahashi = (A+B)*C
    #青木
    Aoki = 0
    Aoki = (D+E)*F
    #比较
    if Takahashi > Aoki:
        print('Takahashi')
    elif Takahashi < Aoki:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()