def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if "ABC" not in s:
        print("ABC")
    elif "AGC" not in s:
        print("AGC")
    elif "ARC" not in s:
        print("ARC")
    else:
        print("AHC")
