def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    s.sort()
    for i in range(3):
        if s[i] == "ABC":
            print("ARC")
        elif s[i] == "ARC":
            print("AGC")
        elif s[i] == "AGC":
            print("AHC")
        elif s[i] == "AHC":
            print("ABC")
        else:
            print("Error")
