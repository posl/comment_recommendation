def main():
    s = input()
    #YYMM
    if int(s[0:2]) <= 12 and int(s[0:2]) >= 1 and int(s[2:4]) <= 12 and int(s[2:4]) >= 1:
        print("AMBIGUOUS")
    elif int(s[0:2]) <= 12 and int(s[0:2]) >= 1:
        print("MMYY")
    elif int(s[2:4]) <= 12 and int(s[2:4]) >= 1:
        print("YYMM")
    else:
        print("NA")

if __name__ == '__main__':
    main()