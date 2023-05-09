def main():
    s = input()
    a = 'atcoder'
    ans = 0
    for i in range(len(s)):
        if s[i] != a[i]:
            ans += abs(ord(s[i]) - ord(a[i]))
    print(ans)
