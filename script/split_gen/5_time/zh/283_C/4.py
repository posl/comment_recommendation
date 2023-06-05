def main():
    s = input()
    n = len(s)
    ans = n
    for i in range(n):
        if s[i] != '0':
            ans = min(ans, i + n - s[::-1].index(s[i]))
    print(ans)
