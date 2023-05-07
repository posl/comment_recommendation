def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if S[0] == "AND":
        ans = 2 ** (N + 1) - 2 ** (N - S.count("AND"))
    else:
        ans = 2 ** (N + 1)
    print(ans)

if __name__ == '__main__':
    main()