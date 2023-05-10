def main():
    S1 = input()
    S2 = input()
    S3 = input()
    contests = ["ABC", "ARC", "AGC", "AHC"]
    contests.remove(S1)
    contests.remove(S2)
    contests.remove(S3)
    print(contests[0])

if __name__ == '__main__':
    main()