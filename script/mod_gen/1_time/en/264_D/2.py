def main():
    s = input()
    atcoder = 'atcoder'
    ans = 0
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()