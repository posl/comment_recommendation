def main():
    s = input()
    first = int(s[:2])
    second = int(s[2:])
    if 0 < first <= 12:
        if 0 < second <= 12:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 0 < second <= 12:
            print("YYMM")
        else:
            print("NA")

if __name__ == '__main__':
    main()