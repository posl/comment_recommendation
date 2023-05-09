def main():
    # input
    A, B, C, D, E = map(int, input().split())
    # compute
    # output
    if (A == B and C == D and B != C) or (A == C and B == D and C != B) or (A == D and B == E and D != B) or (A == E and B == C and A != B) or (A == B and C == E and A != C):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()