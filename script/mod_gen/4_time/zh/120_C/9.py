def main():
    s = input()
    n = len(s)
    s = s[::-1]
    ans = 0
    cnt = 0
    for i in range(n):
        if s[i] == '0':
            cnt += 1
        else:
            ans += min(cnt, i - cnt)
    print(ans)

if __name__ == '__main__':
    main()