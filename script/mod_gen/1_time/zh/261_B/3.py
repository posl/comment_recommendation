def check(n, a):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] != 'L':
                return False

if __name__ == '__main__':
    check()