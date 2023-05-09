def main():
    s = input()
    l = len(s)
    ans = 0
    for i in range(l):
        ans += 26**i
    ans += ord(s[0])-ord('A')
    for i in range(1,l):
        ans += (ord(s[i])-ord('A'))*26**(l-i)
    print(ans+1)

if __name__ == '__main__':
    main()