def main():
    s = input()
    base = 26
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - ord('A') + 1) * pow(base, len(s) - i - 1)
    print(ans)
