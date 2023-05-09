def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC" and s2 == "ARC":
        if s3 == "AGC":
            print("AHC")
        else:
            print("AGC")
    elif s1 == "ABC" and s2 == "AGC":
        if s3 == "ARC":
            print("AHC")
        else:
            print("ARC")
    elif s1 == "ABC" and s2 == "AHC":
        if s3 == "ARC":
            print("AGC")
        else:
            print("ARC")
    elif s1 == "ARC" and s2 == "AGC":
        if s3 == "ABC":
            print("AHC")
        else:
            print("ABC")
    elif s1 == "ARC" and s2 == "AHC":
        if s3 == "ABC":
            print("AGC")
        else:
            print("ABC")
    elif s1 == "AGC" and s2 == "AHC":
        if s3 == "ABC":
            print("ARC")
        else:
            print("ABC")

if __name__ == '__main__':
    main()