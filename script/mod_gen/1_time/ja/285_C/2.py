def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += 26**i * (ord(S[i]) - ord('A') + 1)
    print(ans)

if __name__ == '__main__':
    main()