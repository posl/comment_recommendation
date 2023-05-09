def main():
    s = input()
    ans = 0
    for i in range(1, len(s)):
        ans += 10
    ans += int(s[0]) + len(s) - 1
    print(ans)

if __name__ == '__main__':
    main()