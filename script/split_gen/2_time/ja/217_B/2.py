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
        else:
            print("ARC")
    elif s1 == "ARC":
        if s2 == "ABC":
            if s3 == "AGC":
                print("AHC")
            else:
                print("AGC")
        else:
            print("ABC")
    else:
        if s2 == "ABC":
            if s3 == "ARC":
                print("AHC")
            else:
                print("ARC")
        else:
            print("ABC")
