def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 1<<30
    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(10):
                t = max(t, abs(int(s[i][k]) - int(s[j][k])))
            ans = min(ans, t)
    print(ans)

if __name__ == '__main__':
    main()