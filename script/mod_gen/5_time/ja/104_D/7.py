def main():
    S = input()
    MOD = 10**9 + 7
    n = len(S)
    ans = 0
    a = 0
    b = 0
    c = 0
    for i in range(n):
        if S[i] == 'A':
            a += 1
        elif S[i] == 'B':
            b += 1
        elif S[i] == 'C':
            c += 1
        else:
            ans = (ans + (a * b * c) % MOD) % MOD
            a = (a * 3) % MOD
            b = (b * 3) % MOD
            c = (c * 3) % MOD
    print(ans)

if __name__ == '__main__':
    main()