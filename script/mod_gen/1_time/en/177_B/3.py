def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = 10**9
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()