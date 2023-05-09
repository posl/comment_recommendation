def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC":
        if s2 == "ARC":
            if s3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        elif s2 == "AGC":
            if s3 == "ARC":
                print("AHC")
            else:
                print("ARC")
        else:
            if s3 == "ARC":
                print("AGC")
            else:
                print("ARC")
    elif s1 == "ARC":
        if s2 == "ABC":
            if s3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        elif s2 == "AGC":
            if s3 == "ABC":
                print("AHC")
            else:
                print("ABC")
        else:
            if s3 == "ABC":
                print("AGC")
            else:
                print("ABC")
    else:
        if s2 == "ABC":
            if s3 == "ARC":
                print("AHC")
            else:
                print("ARC")
        elif s2 == "ARC":
            if s3 == "ABC":
                print("AHC")
            else:
                print("ABC")
        else:
            if s3 == "ABC":
                print("ARC")
            else:
                print("ABC")

if __name__ == '__main__':
    main()