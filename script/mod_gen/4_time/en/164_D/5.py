def main():
    s = input()
    n = len(s)
    mod = 2019
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if int(s[i:j+1]) % mod == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()