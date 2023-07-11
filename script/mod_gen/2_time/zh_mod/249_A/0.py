def run():
    A,B,C,D,E,F,X = map(int,input().split())
    takahashi = 0
    aoki = 0
    while True:
        takahashi += A * B
        if takahashi >= X:
            print("Takahashi")
            break
        aoki += D * E
        if aoki >= X:
            print("Aoki")
            break
        takahashi += C * B
        aoki += F * E

if __name__ == '__main__':
    run()