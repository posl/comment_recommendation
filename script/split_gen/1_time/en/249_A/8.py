def main():
    # Read input
    A, B, C, D, E, F, X = map(int, input().split())
    # Calculate distance
    takahashi = (A + C) * B
    aoki = D * E
    # Print output
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
