def main():
    s1 = input()
    s2 = input()
    s3 = input()
    print("ABC" if s1 != "ABC" else "ARC" if s2 != "ARC" else "AGC" if s3 != "AGC" else "AHC")

if __name__ == '__main__':
    main()