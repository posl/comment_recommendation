def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if i == 0 and s[i] == '1':
            ans += 10
        else:
            ans += int(s[i]) + 1
    print(ans)

if __name__ == '__main__':
    main()