def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == "ABC":
        if S2 == "ARC":
            if S3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        else:
            print("ARC")
    elif S1 == "ARC":
        if S2 == "ABC":
            if S3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        else:
            print("ABC")
    else:
        if S2 == "ABC":
            if S3 == "ARC":
                print("AGC")
            else:
                print("ARC")
        else:
            print("ABC")

if __name__ == '__main__':
    main()