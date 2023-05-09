def main():
    s = input()
    n = len(s)
    ans = 26**(n-1)
    ans += sum([26**i*(ord(s[i])-ord('A')+1) for i in range(n)])
    print(ans)

if __name__ == '__main__':
    main()