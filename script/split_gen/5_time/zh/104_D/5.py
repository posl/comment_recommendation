def main():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    ans = 0
    x = 1
    for i in range(n):
        if s[i] == 'B' or s[i] == '?':
            ans += x
        x *= 3
        x %= mod
    x = 1
    for i in range(n-1, -1, -1):
        if s[i] == 'B' or s[i] == '?':
            ans += x * pow(3, s[i+1:].count('?'), mod)
        x *= 3
        x %= mod
    print(ans % mod)
