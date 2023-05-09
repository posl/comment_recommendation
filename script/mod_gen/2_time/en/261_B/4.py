def main():
    n = int(input())
    a = [input() for _ in range(n)]
    ans = 'correct'
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W' and a[j][i] == 'L':
                ans = 'incorrect'
            if a[i][j] == 'L' and a[j][i] == 'W':
                ans = 'incorrect'
            if a[i][j] == 'D' and a[j][i] == 'D':
                ans = 'incorrect'
    print(ans)

if __name__ == '__main__':
    main()