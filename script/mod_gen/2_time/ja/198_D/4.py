def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if len(S1) < len(S3) and len(S2) < len(S3):
        print("UNSOLVABLE")
    else:
        N1 = 0
        N2 = 0
        N3 = 0
        for i in range(len(S1)):
            N1 += (ord(S1[i]) - ord("a") + 1) * 10 ** (len(S1) - i - 1)
        for i in range(len(S2)):
            N2 += (ord(S2[i]) - ord("a") + 1) * 10 ** (len(S2) - i - 1)
        for i in range(len(S3)):
            N3 += (ord(S3[i]) - ord("a") + 1) * 10 ** (len(S3) - i - 1)
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
        else:
            print("UNSOLVABLE")
main()

if __name__ == '__main__':
    main()