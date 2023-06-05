def main():
    S = input()
    Q = S.count('?')
    mod = 10**9 + 7
    ans = 0
    for i in range(len(S)):
        if S[i] == 'B' or S[i] == '?':
            ans += pow(3, Q, mod) * pow(3, i, mod)
            ans %= mod
        if S[i] == 'C' or S[i] == '?':
            ans += pow(3, Q, mod) * pow(3, i, mod)
            ans %= mod
        Q -= 1
    print(ans)

if __name__ == '__main__':
    main()