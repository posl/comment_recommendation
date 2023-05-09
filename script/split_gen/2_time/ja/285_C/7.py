def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l):
        ans += 26 ** i
    ans += sum([ord(s[i]) - ord('A') for i in range(l)]) * 26 ** (l - 1) + 1
    print(ans)
