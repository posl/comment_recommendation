def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans += 1
    print(min(ans, n-ans)*2)

if __name__ == '__main__':
    main()