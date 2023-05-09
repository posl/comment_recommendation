def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
        else:
            if t[i] == 'r' and t[i-k] != 'p':
                ans += p
                t = t[:i] + 'p' + t[i+1:]
            elif t[i] == 's' and t[i-k] != 'r':
                ans += r
                t = t[:i] + 'r' + t[i+1:]
            elif t[i] == 'p' and t[i-k] != 's':
                ans += s
                t = t[:i] + 's' + t[i+1:]
    print(ans)
