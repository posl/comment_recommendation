def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += 26**(n-i-1) * (ord(s[i]) - ord('A') + 1)
    print(ans)
