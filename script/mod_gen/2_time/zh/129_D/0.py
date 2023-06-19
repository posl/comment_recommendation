def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            cnt = 0
            for k in range(i + 1, h):
                if s[k][j] == '#':
                    break
                cnt += 1
            for k in range(i - 1, -1, -1):
                if s[k][j] == '#':
                    break
                cnt += 1
            for k in range(j + 1, w):
                if s[i][k] == '#':
                    break
                cnt += 1
            for k in range(j - 1, -1, -1):
                if s[i][k] == '#':
                    break
                cnt += 1
            ans = max(ans, cnt + 1)
    print(ans)

if __name__ == '__main__':
    main()