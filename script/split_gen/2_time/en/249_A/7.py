def main():
    A,B,C,D,E,F,X = map(int,input().split())
    Takahashi = X//(A+B)*A
    if X%(A+B) < A:
        Takahashi += X%(A+B)
    else:
        Takahashi += A
    Aoki = X//(C+D)*D
    if X%(C+D) < D:
        Aoki += X%(C+D)
    else:
        Aoki += D
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")
