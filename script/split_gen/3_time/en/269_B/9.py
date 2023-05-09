def main():
    # input
    s = []
    for i in range(10):
        s.append(input())
    # compute
    row = [0] * 10
    col = [0] * 10
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                row[i] += 1
                col[j] += 1
    max_row = max(row)
    max_col = max(col)
    # output
    print(max_row, max_col)
