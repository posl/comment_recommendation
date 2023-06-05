def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(10):
        for j in range(i+1, 10):
            cnt = 0
            for k in range(n):
                if s[k][i] == s[k][j]:
                    cnt += 1
            ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()