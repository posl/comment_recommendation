def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    # output
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A < B:
            print("Aoki")
        else:
            print("Takahashi")
