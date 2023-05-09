def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == 'v' and i+1 < len(s) and s[i+1] == 'v':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()