def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = (A + C) * B
    Aoki = D * E
    if Takahashi == Aoki:
        print("Draw")
    elif Takahashi > Aoki:
        print("Takahashi")
    else:
        print("Aoki")
