def main():
    # input
    A, B, C, D, E = map(int, input().split())
    # output
    if (A == B and B == C) or (A == B and B == D) or (A == B and B == E) or (A == C and C == D) or (A == C and C == E) or (A == D and D == E) or (B == C and C == D) or (B == C and C == E) or (B == D and D == E) or (C == D and D == E):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()