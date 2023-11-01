def main():
    A,B,C,D,E,F,X = map(int,input().split())
    # print(A,B,C,D,E,F,X)
    Taka = 0
    Aoki = 0
    while True:
        if X > 0:
            X -= A
            Taka += B
            if X > 0:
                X -= C
            else:
                break
        else:
            break
        if X > 0:
            X -= D
            Aoki +=

if __name__ == '__main__':
    main()