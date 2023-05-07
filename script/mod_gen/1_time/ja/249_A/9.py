def main():
    #input
    A, B, C, D, E, F, X = map(int, input().split())
    #compute
    #output
    if (A * B * C) > (D * E * F):
        print("Takahashi")
    elif (A * B * C) < (D * E * F):
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()