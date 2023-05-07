def main():
    #入力
    X,Y,Z = map(int,input().split())
    #出力
    if X<Z and Z<Y:
        print(Y-X)
    elif X>Z and Z>Y:
        print(X-Y)
    else:
        print(-1)

if __name__ == '__main__':
    main()