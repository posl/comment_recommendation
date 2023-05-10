def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == "ABC" and s2 == "ARC":
        print("AGC")
    elif s1 == "ABC" and s2 == "AGC":
        print("ARC")
    elif s1 == "ABC" and s2 == "AHC":
        print("ARC")
    elif s1 == "ARC" and s2 == "AGC":
        print("ABC")
    elif s1 == "ARC" and s2 == "AHC":
        print("AGC")
    elif s1 == "AGC" and s2 == "AHC":
        print("ARC")
