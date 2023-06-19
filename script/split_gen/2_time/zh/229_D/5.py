def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1] == 'X':
            ans += 1
    ans += min(ans + k, n - 1)
    print(ans)
