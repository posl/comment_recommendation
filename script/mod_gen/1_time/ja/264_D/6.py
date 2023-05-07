def main():
    s = input()
    t = "atcoder"
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += (len(s) - i)
            break
    print(ans)

if __name__ == '__main__':
    main()