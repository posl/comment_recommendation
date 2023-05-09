def main():
    #入力
    X,Y = map(int,input().split())
    #出力
    if 2*X <= Y <= 4*X and Y%2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()