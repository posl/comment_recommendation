def main():
    # Read input data
    S = input()
    # YYMM and MMYY are the two possible formats
    YYMM = "YYMM"
    MMYY = "MMYY"
    # Check if S is valid in YYMM format
    YYMM_valid = False
    if int(S[:2]) >= 1 and int(S[:2]) <= 12:
        if int(S[2:]) >= 1 and int(S[2:]) <= 99:
            YYMM_valid = True
    # Check if S is valid in MMYY format
    MMYY_valid = False
    if int(S[2:]) >= 1 and int(S[2:]) <= 12:
        if int(S[:2]) >= 1 and int(S[:2]) <= 99:
            MMYY_valid = True
    # Output the result
    if YYMM_valid and MMYY_valid:
        print("AMBIGUOUS")
    elif YYMM_valid:
        print(YYMM)
    elif MMYY_valid:
        print(MMYY)
    else:
        print("NA")
main()
Problem 127: B - Algae

if __name__ == '__main__':
    main()