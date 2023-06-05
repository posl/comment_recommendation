def main():
    s = input()
    s = s[::-1]
    ans = 0
    for i in range(len(s)):
        if i == 0:
            ans += int(s[i])
        elif i == 1:
            ans += int(s[i]) * 2
        else:
            ans += int(s[i]) * (i + 1)
    print(ans)

if __name__ == '__main__':
    main()