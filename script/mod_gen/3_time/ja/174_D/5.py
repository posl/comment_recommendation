def main():
    n = int(input())
    s = input()
    ans = 0
    if s[0] == 'W':
        ans += 1
    for i in range(n - 1):
        if s[i] == 'R' and s[i + 1] == 'W':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()