def main():
    S = input()
    #print(S)
    if (int(S[0:2]) > 0 and int(S[0:2]) <= 12) and (int(S[2:4]) > 0 and int(S[2:4]) <= 12):
        print("AMBIGUOUS")
    elif (int(S[0:2]) > 0 and int(S[0:2]) <= 12) and (int(S[2:4]) > 12 and int(S[2:4]) <= 99):
        print("MMYY")
    elif (int(S[0:2]) > 12 and int(S[0:2]) <= 99) and (int(S[2:4]) > 0 and int(S[2:4]) <= 12):
        print("YYMM")
    elif (int(S[0:2]) > 12 and int(S[0:2]) <= 99) and (int(S[2:4]) > 12 and int(S[2:4]) <= 99):
        print("NA")

if __name__ == '__main__':
    main()