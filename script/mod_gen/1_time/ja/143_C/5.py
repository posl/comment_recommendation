def main():
    N = int(input())
    S = input()
    print(N - S.count(S[0]) - S.count(S[-1]) + 1)

if __name__ == '__main__':
    main()