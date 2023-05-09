def main():
    S = input()
    N = len(S)
    Q = S.count("?")
    MOD = 10 ** 9 + 7
    ans = 0
    for i in range(N):
        if S[i] == "A":
            a = 1
        elif S[i] == "B":
            a = 2
        elif S[i] == "C":
            a = 3
        else:
            a = 0
        if a > 0:
            ans += a * pow(3, Q, MOD) * pow(3, i, MOD)
            ans %= MOD
        Q -= 1
    print(ans)

if __name__ == '__main__':
    main()