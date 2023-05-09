def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += (ord(s[i]) - ord('A')) * pow(26, n - i - 1)
    print(ans + 1)
