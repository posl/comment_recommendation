def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            if s[i][j] == '#':
                if s[i+1][j] == '#' or s[i][j+1] == '#' or s[i+1][j+1] == '#':
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()