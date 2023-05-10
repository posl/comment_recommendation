def main():
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    if k == m - 1:
                        ans += 1
                    else:
                        continue
                else:
                    break
    print(ans)

if __name__ == '__main__':
    main()