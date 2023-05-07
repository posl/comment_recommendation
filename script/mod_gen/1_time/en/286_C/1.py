def main():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n//2):
        if s[i] == s[-(i+1)]:
            continue
        elif s[i] == 'a' and s[-(i+1)] != 'a':
            ans += a
        elif s[i] != 'a' and s[-(i+1)] == 'a':
            ans += a
        elif s[i] == 'b' and s[-(i+1)] != 'b':
            ans += b
        elif s[i] != 'b' and s[-(i+1)] == 'b':
            ans += b
        else:
            ans = -1
            break
    else:
        if s[n//2] != 'a' and s[n//2] != 'b':
            ans += min(a, b)
    print(ans)

if __name__ == '__main__':
    main()