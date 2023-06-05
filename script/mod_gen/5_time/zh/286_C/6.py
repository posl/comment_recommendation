def main():
    n, a, b = map(int, input().split())
    s = input()
    cnt = 0
    for i in range(n):
        if s[i] != s[n-i-1]:
            if s[i] == 'a':
                cnt += a
            else:
                cnt += b
        elif s[i] == s[n-i-1] and s[i] == 'a':
            cnt += a
        elif s[i] == s[n-i-1] and s[i] == 'b':
            cnt += b
    print(cnt)

if __name__ == '__main__':
    main()