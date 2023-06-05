def main():
    s = input()
    t = input()
    n = len(s)
    ans = n
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i + j < n:
                if s[i + j] != t[j]:
                    cnt += 1
            else:
                if s[i + j - n] != t[j]:
                    cnt += 1
        ans = min(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()