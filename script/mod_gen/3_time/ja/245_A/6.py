def main():
    A, B, C, D = map(int, input().split())
    if A < C or (A == C and B <= D):
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()