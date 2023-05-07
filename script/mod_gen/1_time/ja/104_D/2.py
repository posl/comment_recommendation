def main():
    S = input()
    MOD = 10**9 + 7
    n = len(S)
    abc = [0] * n
    for i in range(n):
        if S[i] == 'A':
            abc[i] = 1
        elif S[i] == 'B':
            abc[i] = 2
        elif S[i] == 'C':
            abc[i] = 3
    #print(abc)
    cnt = [0, 0, 0, 0]
    for i in range(n):
        cnt[abc[i]] += 1
    #print(cnt)
    ans = 0
    q = S.count('?')
    for i in range(n):
        if abc[i] == 0:
            ans += cnt[1] * pow(3, q - 1, MOD) + cnt[2] * pow(3, q - 1, MOD) + cnt[3] * pow(3, q - 1, MOD)
            ans %= MOD
            q -= 1
        elif abc[i] == 1:
            ans += cnt[2] * pow(3, q, MOD) + cnt[3] * pow(3, q, MOD)
            ans %= MOD
        elif abc[i] == 2:
            ans += cnt[1] * pow(3, q, MOD) + cnt[3] * pow(3, q, MOD)
            ans %= MOD
        elif abc[i] == 3:
            ans += cnt[1] * pow(3, q, MOD) + cnt[2] * pow(3, q, MOD)
            ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()