def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if s.count("ABC") == 0:
        print("ABC")
    elif s.count("ARC") == 0:
        print("ARC")
    elif s.count("AGC") == 0:
        print("AGC")
    elif s.count("AHC") == 0:
        print("AHC")

if __name__ == '__main__':
    main()