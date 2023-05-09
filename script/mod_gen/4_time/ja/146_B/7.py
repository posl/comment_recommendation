def main():
    n = int(input())
    s = input()
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    for i in range(len(s)):
        ans += alp[(alp.index(s[i]) + n) % 26]
    print(ans)

if __name__ == '__main__':
    main()