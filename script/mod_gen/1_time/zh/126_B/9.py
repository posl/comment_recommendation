def main():
    S = input()
    S1 = int(S[0:2])
    S2 = int(S[2:4])
    if 1 <= S1 <= 12 and 1 <= S2 <= 12:
        print("AMBIGUOUS")
    elif 1 <= S1 <= 12 and not 1 <= S2 <= 12:
        print("MMYY")
    elif not 1 <= S1 <= 12 and 1 <= S2 <= 12:
        print("YYMM")
    else:
        print("NA")

if __name__ == '__main__':
    main()