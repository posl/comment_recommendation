def main():
    S1 = input()
    S2 = input()
    S3 = input()
    # Check the length of S1, S2, S3
    if len(S1) < 1 or len(S1) > 10 or len(S2) < 1 or len(S2) > 10 or len(S3) < 1 or len(S3) > 10:
        print("UNSOLVABLE")
        return
    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S1[i] < 'a' or S1[i] > 'z' or S2[i] < 'a' or S2[i] > 'z' or S3[i] < 'a' or S3[i] > 'z':
            print("UNSOLVABLE")
            return
    # Check the length of S1, S2, S3
    if len(S1) != len(S2) or len(S1) != len(S3) or len(S2) != len(S3):
        print("UNSOLVABLE")
        return
    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S1[i] == S2[i] and S1[i] != S3[i]:
            print("UNSOLVABLE")
            return
    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S1[i] == S3[i] and S1[i] != S2[i]:
            print("UNSOLVABLE")
            return
    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S2[i] == S3[i] and S1[i] != S2[i]:
            print("UNSOLVABLE")
            return
    # Check the character of S1, S2, S3
    for i in range(len(S1)):
        if S1[i] == S2[i] and S2[i] == S3[i]:
            if i == 0:
                if len(S1) == 1:
                    print(1)
                    print(1)
                    print(2)
                    return
                else:
                    print("UNSOLV

if __name__ == '__main__':
    main()