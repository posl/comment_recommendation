def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = (A + C) * B
    aoki = D * E
    if takahashi > aoki:
        print("Takahashi")
    elif aoki > takahashi:
        print("Aoki")
    else:
        print("Draw")
