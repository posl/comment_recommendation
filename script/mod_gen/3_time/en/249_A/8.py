def jog(A,B,C,D,E,F,X):
    Takahashi = 0
    Aoki = 0
    for i in range(1,X):
        if i % (A+C) in range(1,A+1):
            Takahashi += B
        if i % (D+F) in range(1,D+1):
            Aoki += E
    if Takahashi > Aoki:
        return "Takahashi"
    elif Aoki > Takahashi:
        return "Aoki"
    else:
        return "Draw"
A,B,C,D,E,F,X = map(int, input().split())
print(jog(A,B,C,D,E,F,X))

if __name__ == '__main__':
    jog()