def main():
    n, k = map(int, input().split())
    s = input()
    r = [0] * (n + 1)
    l = [0] * (n + 1)
    for i in range(n):
        if s[i] == 'R':
            r[i + 1] = r[i] + 1
            l[i + 1] = 0
        else:
            l[i + 1] = l[i] + 1
            r[i + 1] = 0
    ans = 0
    for i in range(n + 1):
        ans = max(ans, min(r[i], k) + min(l[i], k))
    for i in range(n):
        if s[i] == s[i + 1]:
            ans += 1
    print(ans)
