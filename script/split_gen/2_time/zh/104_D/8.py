def main():
    s = input()
    q = s.count('?')
    ans = 0
    mod = 10**9+7
    for i in range(len(s)):
        if s[i] == 'B' or s[i] == '?':
            ans += pow(3,q,mod) * pow(3,i,mod)
            q -= 1
        if s[i] == 'C' or s[i] == '?':
            ans += pow(3,q,mod) * pow(3,i,mod)
            q -= 1
    print(ans%mod)
