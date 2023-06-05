def main():
    S = input()
    Q = S.count('?')
    MOD = 10 ** 9 + 7
    S = S.replace('?', '0')
    ans = 0
    for i in range(len(S)):
        if S[i] == 'A':
            ans += pow(3, Q, MOD)
        elif S[i] == 'B':
            ans += pow(3, Q, MOD) * pow(2, i, MOD)
        elif S[i] == 'C':
            ans += pow(3, Q, MOD) * pow(2, i, MOD) * pow(2, len(S) - i - 1, MOD)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()