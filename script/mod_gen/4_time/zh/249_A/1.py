def main():
    A,B,C,D,E,F,X = map(int,input().split())
    taka = 0
    aoki = 0
    while True:
        if taka >= X:
            print("DRAW")
            break
        elif aoki >= X:
            print("TAKAHASHI")
            break
        taka += A
        aoki += D
        if taka >= X:
            print("TAKAHASHI")
            break
        elif aoki >= X:
            print("AOKI")
            break
        taka += B
        aoki += E
        if taka >= X:
            print("TAKAHASHI")
            break
        elif aoki >= X:
            print("AOKI")
            break
        taka += C
        aoki += F

if __name__ == '__main__':
    main()