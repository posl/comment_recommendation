def main():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n//2):
        if s[i] == s[-(i+1)]:
            continue
        if s[i] == 'a':
            ans += a
        elif s[i] == 'b':
            ans += b
        elif s[-(i+1)] == 'a':
            ans += a
        elif s[-(i+1)] == 'b':
            ans += b
        else:
            print(-1)
            return
    if n % 2 == 1:
        if s[n//2] == 'a':
            ans += a
        elif s[n//2] == 'b':
            ans += b
    print(ans)
