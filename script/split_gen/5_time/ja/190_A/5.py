def main():
    #input
    A, B, C = map(int, input().split())
    #compute
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")
    #output
