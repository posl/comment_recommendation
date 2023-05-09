def main():
    s = input().strip()
    n = len(s)
    ans = 0
    if n < 4:
        print(0)
        return
    for i in range(n-3):
        for j in range(i+3, n+1):
            if int(s[i:j]) % 2019 == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()