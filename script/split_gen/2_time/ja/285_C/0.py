def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - i - 1)
    print(ans)
