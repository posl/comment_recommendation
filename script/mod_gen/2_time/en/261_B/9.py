def solve():
    n = int(input())
    a = [list(input()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] == 'L':
                    return 'incorrect'
            elif a[i][j] == 'L':
                if a[j][i] == 'W':
                    return 'incorrect'
            elif a[i][j] == 'D':
                if a[j][i] == 'D':
                    return 'incorrect'
    return 'correct'
print(solve())

if __name__ == '__main__':
    solve()