def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i >= k and t[i] == t[i - k] and t[i - k] != 'x':
            t = t[:i] + 'x' + t[i + 1:]
        else:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
    print(ans)
