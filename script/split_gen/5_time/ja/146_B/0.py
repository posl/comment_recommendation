def main():
    n = int(input())
    s = input()
    ans = ""
    for i in range(len(s)):
        ans += chr(65 + (ord(s[i]) - 65 + n) % 26)
    print(ans)
