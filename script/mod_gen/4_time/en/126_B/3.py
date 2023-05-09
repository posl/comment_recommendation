def main():
    S = input()
    YY = int(S[0:2])
    MM = int(S[2:4])
    if (0 < MM and MM < 13) and (0 < YY and YY < 13):
        print("AMBIGUOUS")
    elif (0 < MM and MM < 13) and (not (0 < YY and YY < 13)):
        print("MMYY")
    elif (not (0 < MM and MM < 13)) and (0 < YY and YY < 13):
        print("YYMM")
    else:
        print("NA")

if __name__ == '__main__':
    main()