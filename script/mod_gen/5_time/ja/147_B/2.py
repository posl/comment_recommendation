def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] != s[n-i-1]:
            ans += 1
    print(ans // 2)

if __name__ == '__main__':
    main()