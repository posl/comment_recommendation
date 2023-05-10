def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if t[i] == 'r':
            if i - k >= 0 and t[i - k] == 'r':
                t = t[:i] + 'x' + t[i + 1:]
            else:
                ans += p
        elif t[i] == 's':
            if i - k >= 0 and t[i - k] == 's':
                t = t[:i] + 'x' + t[i + 1:]
            else:
                ans += r
        elif t[i] == 'p':
            if i - k >= 0 and t[i - k] == 'p':
                t = t[:i] + 'x' + t[i + 1:]
            else:
                ans += s
    print(ans)
