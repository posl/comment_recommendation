def main():
    s = input()
    if (int(s[0:2]) >= 1) and (int(s[0:2]) <= 12):
        if (int(s[2:4]) >= 1) and (int(s[2:4]) <= 12):
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if (int(s[2:4]) >= 1) and (int(s[2:4]) <= 12):
            print("YYMM")
        else:
            print("NA")

if __name__ == '__main__':
    main()