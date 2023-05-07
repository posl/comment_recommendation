def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(10 * (N - 1) + min(S[0].index(s) for s in S[0]))

if __name__ == '__main__':
    main()