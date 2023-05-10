def main():
    s = input()
    t = input()
    ans = len(s)
    for i in range(len(s)):
        if s[i:] + s[:i] == t:
            ans = min(ans, i)
    print(ans)

if __name__ == '__main__':
    main()