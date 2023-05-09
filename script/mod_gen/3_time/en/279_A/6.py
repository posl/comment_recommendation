def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == "v":
            ans += len(s[i+1:]) - s[i+1:].count("v")
    print(ans)

if __name__ == '__main__':
    main()