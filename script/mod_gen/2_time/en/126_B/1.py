def main():
    S = input()
    if int(S[2:]) <= 12 and int(S[:2]) <= 12:
        print("AMBIGUOUS")
    elif int(S[2:]) <= 12:
        print("YYMM")
    elif int(S[:2]) <= 12:
        print("MMYY")
    else:
        print("NA")

if __name__ == '__main__':
    main()