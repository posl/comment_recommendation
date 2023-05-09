def main():
    s = input()
    yymm = s[0:2]
    mmyy = s[2:4]
    if 0 < int(yymm) <= 12 and 0 < int(mmyy) <= 12:
        print("AMBIGUOUS")
    elif 0 < int(yymm) <= 12:
        print("YYMM")
    elif 0 < int(mmyy) <= 12:
        print("MMYY")
    else:
        print("NA")

if __name__ == '__main__':
    main()