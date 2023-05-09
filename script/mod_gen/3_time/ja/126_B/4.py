def main():
    S = input()
    if S[0] == "0" and S[1] == "0":
        if S[2] == "0" and S[3] == "0":
            print("NA")
        elif 1 <= int(S[2]) and int(S[2]) <= 9 and 0 <= int(S[3]) and int(S[3]) <= 9:
            print("YYMM")
        elif 1 <= int(S[3]) and int(S[3]) <= 9 and 0 <= int(S[2]) and int(S[2]) <= 9:
            print("MMYY")
        else:
            print("NA")
    elif 1 <= int(S[0]) and int(S[0]) <= 9 and 0 <= int(S[1]) and int(S[1]) <= 9:
        if S[2] == "0" and S[3] == "0":
            print("YYMM")
        elif 1 <= int(S[2]) and int(S[2]) <= 9 and 0 <= int(S[3]) and int(S[3]) <= 9:
            print("AMBIGUOUS")
        elif 1 <= int(S[3]) and int(S[3]) <= 9 and 0 <= int(S[2]) and int(S[2]) <= 9:
            print("AMBIGUOUS")
        else:
            print("YYMM")
    elif 1 <= int(S[1]) and int(S[1]) <= 9 and 0 <= int(S[0]) and int(S[0]) <= 9:
        if S[2] == "0" and S[3] == "0":
            print("MMYY")
        elif 1 <= int(S[2]) and int(S[2]) <= 9 and 0 <= int(S[3]) and int(S[3]) <= 9:
            print("MMYY")
        elif 1 <= int(S[3]) and int(S[3]) <= 9 and 0 <= int(S[2]) and int(S[2]) <= 9:
            print("AMBIGUOUS")
        else:
            print("NA")
    else:
        print("NA")

if __name__ == '__main__':
    main()