def main():
    S = input()
    if int(S[0:2]) > 0 and int(S[0:2]) < 13:
        if int(S[2:4]) > 0 and int(S[2:4]) < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    elif int(S[2:4]) > 0 and int(S[2:4]) < 13:
        print("YYMM")
    else:
        print("NA")

if __name__ == '__main__':
    main()