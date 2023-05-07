def main():
    A,B,C,D,E,F,X = map(int,input().split())
    Takahashi = 0
    Aoki = 0
    Takahashi = (A+B)*C
    Aoki = (D+E)*F
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")
