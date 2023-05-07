def main():
    #input
    A, B, C, D, E = map(int, input().split())
    #output
    if (A == B == C and D != E) or (A == B == D and C != E) or (A == B == E and C != D) or (A == C == D and B != E) or (A == C == E and B != D) or (A == D == E and B != C) or (B == C == D and A != E) or (B == C == E and A != D) or (B == D == E and A != C) or (C == D == E and A != B):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()