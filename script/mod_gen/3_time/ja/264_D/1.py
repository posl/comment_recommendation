def main():
    s = input()
    ans = 0
    atcoder = 'atcoder'
    for i in range(len(s)):
        if s[i] != atcoder[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()