def main():
    A, B, C, D, E, F, X = map(int, input().split())
    if (A > B):
        A = B
    if (D > E):
        D = E
    if (X <= A):
        print("Takahashi")
    elif (X <= D):
        print("Draw")
    else:
        if (B > E):
            print("Takahashi")
        elif (B < E):
            print("Aoki")
        else:
            print("Draw")
