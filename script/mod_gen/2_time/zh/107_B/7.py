def find_column(a, j):
    for i in range(len(a)):
        if a[i][j] == '#':
            return False
    return True

if __name__ == '__main__':
    find_column()