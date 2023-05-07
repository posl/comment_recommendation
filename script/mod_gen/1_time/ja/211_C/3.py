def main():
    S = input()
    MOD = 10**9 + 7
    ans = 1
    c = 0
    for i in range(len(S)):
        if S[i] == "c":
            c += 1
        elif S[i] == "h" and c > 0:
            ans *= c
            ans %= MOD
            c -= 1
        elif S[i] == "o" and c > 0:
            ans *= c
            ans %= MOD
            c -= 1
        elif S[i] == "k" and c > 0:
            ans *= c
            ans %= MOD
            c -= 1
        elif S[i] == "u" and c > 0:
            ans *= c
            ans %= MOD
            c -= 1
        elif S[i] == "d" and c > 0:
            ans *= c
            ans %= MOD
            c -= 1
        elif S[i] == "a" and c > 0:
            ans *= c
            ans %= MOD
            c -= 1
        elif S[i] == "i" and c > 0:
            ans *= c
            ans %= MOD
            c -= 1
    print(ans)

if __name__ == '__main__':
    main()