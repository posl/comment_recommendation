def main():
    s = input()
    t = 'atcoder'
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] != t[i]:
            ans += n - i - 1
    print(ans)
