def main():
    S1 = input()
    S2 = input()
    S3 = input()
    S = [S1, S2, S3]
    T = ["ABC", "ARC", "AGC", "AHC"]
    for s in S:
        T.remove(s)
    print(T[0])

if __name__ == '__main__':
    main()