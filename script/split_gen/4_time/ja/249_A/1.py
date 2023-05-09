def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = 0
    aoki = 0
    for i in range(1, X+1):
        if i % (A+C) <= A:
            takahashi += B
        if i % (D+F) <= D:
            aoki += E
    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")
