def main():
    s = input()
    ans = -1
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            ans = s[i]
    print(ans)

if __name__ == '__main__':
    main()