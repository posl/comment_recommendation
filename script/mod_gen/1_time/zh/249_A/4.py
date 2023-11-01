def main():
    A,B,C,D,E,F,X = map(int,input().split())
    Takahashi = 0
    Aoki = 0
    for i in range(X):
        if i % (A + B) < A:
            Takahashi += E
        if i % (C + D) < C:
            Aoki += F

if __name__ == '__main__':
    main()