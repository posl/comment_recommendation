def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                if i > 0 and s[i-1][j] == '-':
                    ans += 1
                if i < h-1 and s[i+1][j] == '-':
                    ans += 1
                if j > 0 and s[i][j-1] == '-':
                    ans += 1
                if j < w-1 and s[i][j+1] == '-':
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()