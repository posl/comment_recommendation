def main():
    s = input()
    q = s.count('?')
    mod = 10**9+7
    l = len(s)
    ans = 0
    for i in range(l):
        if s[i] == 'C':
            ans += pow(3,q,mod)*pow(3,i,mod)
            ans %= mod
        elif s[i] == 'B':
            ans += pow(3,q,mod)*pow(3,i,mod)
            ans %= mod
            q -= 1
        elif s[i] == 'A':
            ans += pow(3,q,mod)*pow(3,i,mod)
            ans %= mod
            q -= 1
            q -= s[i+1:].count('?')
    print(ans)

if __name__ == '__main__':
    main()