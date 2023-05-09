def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += (ord(S[i])-64)
        else:
            ans += (ord(S[i])-64) * (26**i)
    print(ans)

if __name__ == '__main__':
    main()