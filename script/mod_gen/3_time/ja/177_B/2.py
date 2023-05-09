def main():
    s = input()
    t = input()
    n = len(t)
    ans = n
    for i in range(len(s)-n+1):
        cnt = 0
        for j in range(n):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()