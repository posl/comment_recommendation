def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i])-64)*26**(len(s)-i-1)
    print(ans)

if __name__ == '__main__':
    main()