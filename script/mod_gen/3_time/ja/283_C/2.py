def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == '0':
            ans += 1
        else:
            ans += 2
    print(ans)

if __name__ == '__main__':
    main()