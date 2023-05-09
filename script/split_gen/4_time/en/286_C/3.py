def main():
    # input
    n, a, b = map(int, input().split())
    s = input()
    # compute
    ans = 0
    for i in range(n//2):
        if s[i] == s[n-1-i]:
            continue
        elif s[i] == 'a':
            if s[n-1-i] == 'b':
                ans += a
            else:
                ans += b
        elif s[i] == 'b':
            if s[n-1-i] == 'a':
                ans += a
            else:
                ans += b
        else:
            if s[n-1-i] == 'a':
                ans += b
            else:
                ans += a
    # output
    print(ans)
