def main():
    n, a, b = map(int, input().split())
    s = input()
    res = 0
    for i in range(n):
        if s[i] == s[n - i - 1]:
            continue
        elif s[i] == 'a':
            if s[n - i - 1] == 'b':
                res += a
            else:
                res += b
        elif s[i] == 'b':
            if s[n - i - 1] == 'a':
                res += a
            else:
                res += b
        else:
            if s[n - i - 1] == 'a':
                res += b
            else:
                res += a
    print(res)

if __name__ == '__main__':
    main()