def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            count = 0
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    count += 1
            if count == m:
                ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()