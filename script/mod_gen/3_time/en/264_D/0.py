def main():
    s = input()
    t = 'atcoder'
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += abs(ord(s[i]) - ord(t[i]))
    print(ans)
main()
