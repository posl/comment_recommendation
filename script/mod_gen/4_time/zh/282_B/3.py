def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = True
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    continue
                else:
                    flag = False
                    break
            if flag:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()