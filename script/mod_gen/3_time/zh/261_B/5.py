def check():
    n = int(raw_input())
    data = []
    for i in range(n):
        data.append(raw_input())
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if data[i][j] == 'W' and data[j][i] != 'L':
                return False
            if data[i][j] == 'L' and data[j][i] != 'W':
                return False
            if data[i][j] == 'D' and data[j][i] != 'D':
                return False
    return True

if __name__ == '__main__':
    check()