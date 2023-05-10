def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    while X > 0:
        if Takahashi + B * A >= Aoki + D * E:
            Takahashi += B * A
            X -= A
            if X <= 0:
                break
            else:
                X -= C
        else:
            Aoki += D * E
            X -= D
            if X <= 0:
                break
            else:
                X -= F
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")
