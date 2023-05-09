def main():
    s = input()
    mod = 2019
    l = len(s)
    ans = 0
    for i in range(l):
        for j in range(i+1,l+1):
            num = int(s[i:j])
            if num % mod == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()