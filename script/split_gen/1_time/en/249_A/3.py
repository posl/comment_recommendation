def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = A * B + C * B
    aoki = D * E + F * E
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
