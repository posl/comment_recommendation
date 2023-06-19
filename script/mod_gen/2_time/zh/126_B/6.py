def main():
    s = input()
    s1 = s[0:2]
    s2 = s[2:4]
    if int(s1) > 12 or int(s1) == 0:
        if int(s2) > 12 or int(s2) == 0:
            print("NA")
        else:
            print("YYMM")
    elif int(s2) > 12 or int(s2) == 0:
        if int(s1) > 12 or int(s1) == 0:
            print("NA")
        else:
            print("MMYY")
    else:
        print("AMBIGUOUS")

if __name__ == '__main__':
    main()