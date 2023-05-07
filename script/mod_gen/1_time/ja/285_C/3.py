def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += (ord(s[i])-64) * 26**(n-i-1)
    print(ans)

if __name__ == '__main__':
    main()