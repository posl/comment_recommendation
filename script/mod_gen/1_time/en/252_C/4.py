def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(10):
        ans = max(ans, sum(s[j][i] == s[0][i] for j in range(n)))
    print(10 - ans)

if __name__ == '__main__':
    main()