def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC":
        if s2 == "ARC":
            print("AGC")
        else:
            print("ARC")
    if s1 == "ARC":
        if s2 == "ABC":
            print("AGC")
        else:
            print("ABC")
    if s1 == "AGC":
        if s2 == "ABC":
            print("ARC")
        else:
            print("ABC")
    if s1 == "AHC":
        if s2 == "ABC":
            print("ARC")
        else:
            print("ABC")
