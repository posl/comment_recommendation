def main():
    S = input()
    S1 = S[0:2]
    S2 = S[2:4]
    if(1 <= int(S1) <= 12 and 1 <= int(S2) <= 12):
        print("AMBIGUOUS")
    elif(1 <= int(S1) <= 12 and not(1 <= int(S2) <= 12)):
        print("MMYY")
    elif(not(1 <= int(S1) <= 12) and 1 <= int(S2) <= 12):
        print("YYMM")
    else:
        print("NA")

if __name__ == '__main__':
    main()