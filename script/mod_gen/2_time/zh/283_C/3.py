def main():
    s = input()
    s = s[::-1]
    ans = 0
    for i in range(0, len(s)):
        if s[i] == "0":
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()