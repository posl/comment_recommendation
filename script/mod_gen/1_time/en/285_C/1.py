def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += (26**i)*(ord(s[n-i-1])-ord('A')+1)
    print(ans)

if __name__ == '__main__':
    main()