def main():
    s = input()
    t = input()
    m = len(s)
    n = len(t)
    ans = n
    for i in range(m-n+1):
        cnt = 0
        for j in range(n):
            if t[j] != s[i+j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()