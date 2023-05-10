def main():
    # input
    A, B, C, D, E, F, X = map(int, input().split())
    # compute
    # output
    if (A * B) > (D * E):
        print("Takahashi")
    elif (A * B) < (D * E):
        print("Aoki")
    else:
        print("Draw")
