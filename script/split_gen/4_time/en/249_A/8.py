def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = B * (A + C) * (X // (A + C))
    if X % (A + C) > A:
        Takahashi += B * A
    else:
        Takahashi += B * (X % (A + C))
    Aoki = E * (D + F) * (X // (D + F))
    if X % (D + F) > D:
        Aoki += E * D
    else:
        Aoki += E * (X % (D + F))
    if Takahashi > Aoki:
        print("Takahashi")
    elif Aoki > Takahashi:
        print("Aoki")
    else:
        print("Draw")
