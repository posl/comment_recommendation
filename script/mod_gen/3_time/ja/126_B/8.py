def main():
    s = input()
    s1 = s[0:2]
    s2 = s[2:4]
    if int(s1) in range(1,13) and int(s2) in range(1,13):
        print("AMBIGUOUS")
    elif int(s1) in range(1,13) and int(s2) in range(13,99):
        print("MMYY")
    elif int(s1) in range(13,99) and int(s2) in range(1,13):
        print("YYMM")
    else:
        print("NA")

if __name__ == '__main__':
    main()