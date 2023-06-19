def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    break
            else:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()