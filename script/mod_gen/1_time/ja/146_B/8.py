def main():
    n = int(input())
    s = input()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    for i in range(len(s)):
        for j in range(len(alpha)):
            if s[i] == alpha[j]:
                ans += alpha[(j+n)%26]
    print(ans)

if __name__ == '__main__':
    main()