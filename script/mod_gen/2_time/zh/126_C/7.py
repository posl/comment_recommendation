def main():
    S = input()
    s1 = S[:2]
    s2 = S[2:]
    if (int(s1) in range(1, 13)) and (int(s2) in range(1, 13)):
        print("AMBIGUOUS")
    elif (int(s1) in range(1, 13)) and (int(s2) not in range(1, 13)):
        print("MMYY")
    elif (int(s1) not in range(1, 13)) and (int(s2) in range(1, 13)):
        print("YYMM")
    else:
        print("NA")

if __name__ == '__main__':
    main()