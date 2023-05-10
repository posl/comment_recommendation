def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - 64) * (26 ** (len(s) - 1 - i))
    print(ans)
