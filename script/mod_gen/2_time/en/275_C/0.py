def main():
    s = [input() for _ in range(9)]
    ans = 0
    for i in range(8):
        for j in range(8):
            if s[i][j] == '#' and s[i][j + 1] == '#' and s[i + 1][j] == '#' and s[i + 1][j + 1] == '#':
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()