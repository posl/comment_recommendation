def main():
    S = input()
    s1 = int(S[0:2])
    s2 = int(S[2:4])
    if 0 < s1 and s1 < 13:
        if 0 < s2 and s2 < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 0 < s2 and s2 < 13:
            print("YYMM")
        else:
            print("NA")

if __name__ == '__main__':
    main()