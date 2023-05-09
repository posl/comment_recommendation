def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = 0
    aoki = 0
    takahashi = (A + B) * (X // (A + C)) + min(A, X % (A + C))
    aoki = (D + E) * (X // (D + F)) + min(D, X % (D + F))
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
