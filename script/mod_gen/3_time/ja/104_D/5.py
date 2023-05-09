def main():
    s = input()
    n = len(s)
    q = s.count("?")
    MOD = 10**9 + 7
    ans = 0
    for i in range(n):
        if s[i] == "A":
            a = 1
        elif s[i] == "B":
            a = 2
        elif s[i] == "C":
            a = 3
        else:
            a = 0
        if a != 0:
            ans += a * pow(3, q, MOD) * pow(3, i, MOD)
            ans %= MOD
            q -= 1
    print(ans)

if __name__ == '__main__':
    main()