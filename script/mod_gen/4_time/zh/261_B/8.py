def solve(n, a):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'W':
                if a[j][i] != 'L':
                    return '不正确'
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    return '不正确'
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    return '不正确'
    return '正确'

if __name__ == '__main__':
    solve()