def main():
    # Read input
    S1 = input()
    S2 = input()
    S3 = input()
    # Solve
    S = ["ABC", "ARC", "AGC", "AHC"]
    S.remove(S1)
    S.remove(S2)
    S.remove(S3)
    # Output
    print(S[0])

if __name__ == '__main__':
    main()