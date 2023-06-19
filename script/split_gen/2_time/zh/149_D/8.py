def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if t[i] == 'r':
            if i < k:
                ans += p
            elif t[i - k] == 'r':
                ans += 0
            else:
                ans += p
        elif t[i] == 's':
            if i < k:
                ans += r
            elif t[i - k] == 's':
                ans += 0
            else:
                ans += r
        elif t[i] == 'p':
            if i < k:
                ans += s
            elif t[i - k] == 'p':
                ans += 0
            else:
                ans += s
    print(ans)
