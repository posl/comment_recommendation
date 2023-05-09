def main():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    S = [S1, S2, S3]
    print("".join([S[int(t)-1] for t in T]))

if __name__ == '__main__':
    main()