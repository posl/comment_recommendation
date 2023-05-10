def main():
    S = input()
    N = len(S)
    Q = S.count("?")
    mod = 10**9 + 7
    ans = 0
    for i, s in enumerate(S):
        if s == "B" or s == "?":
            ans += pow(3, Q, mod) * pow(3, i, mod) * pow(2, N-i-1, mod)
            ans %= mod
        if s == "?":
            Q -= 1
    print(ans)

if __name__ == '__main__':
    main()