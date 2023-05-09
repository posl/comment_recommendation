def main():
    A,B,C,D,E,F,X = map(int, input().split())
    T = 0
    Aoki = 0
    Takahashi = 0
    while T < X:
        if T % (A+C) < A:
            Takahashi += B
        if T % (D+F) < D:
            Aoki += E
        T += 1
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")
