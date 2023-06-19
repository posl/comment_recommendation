def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    for i in ["ABC", "ARC", "AGC", "AHC"]:
        if i not in s:
            print(i)
main()
