def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    N = len(S1)
    if N != len(S2) or N != len(S3):
        print("UNSOLVABLE")
        return
    if N == 1:
        if S1 == S2 and S2 == S3:
            print("0")
            print("0")
            print("0")
        else:
            print("UNSOLVABLE")
        return
    if N == 2:
        if S1[0] == S2[0] and S2[0] == S3[0]:
            print("0", end="")
        elif S1[0] == S2[0]:
            print("0", end="")
        elif S1[0] == S3[0]:
            print("0", end="")
        elif S2[0] == S3[0]:
            print("0", end="")
        else:
            print("1", end="")
        if S1[1] == S2[1] and S2[1] == S3[1]:
            print("0", end="")
        elif S1[1] == S2[1]:
            print("0", end="")
        elif S1[1] == S3[1]:
            print("0", end="")
        elif S2[1] == S3[1]:
            print("0", end="")
        else:
            print("1", end="")
        print()
        if S1[0] == S2[0] and S2[0] == S3[0]:
            print("0", end="")
        elif S1[0] == S2[0]:
            print("0", end="")
        elif S1[0] == S3[0]:
            print("0", end="")
        elif S2[0] == S3[0]:
            print("0", end="")
        else:
            print("1", end="")
        if S1[1] == S2[1] and S2[1] == S3[1]:
            print("0", end="")
        elif S1[1] == S2[1]:
            print("0", end="")
        elif S1[1] == S3[1]:
            print("0", end="")
        elif S2[1] == S
