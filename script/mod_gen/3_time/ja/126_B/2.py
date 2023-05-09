def main():
    s = input()
    if s[0] == "0" and s[1] == "0":
        if s[2] == "0" and s[3] == "0":
            print("NA")
        else:
            print("YYMM")
    elif s[2] == "0" and s[3] == "0":
        print("MMYY")
    elif int(s[0]) > 1:
        if int(s[2]) > 1:
            print("NA")
        else:
            print("YYMM")
    elif int(s[2]) > 1:
        if int(s[0]) > 1:
            print("NA")
        else:
            print("MMYY")
    else:
        print("AMBIGUOUS")

if __name__ == '__main__':
    main()