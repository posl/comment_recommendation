def rotate90(figure):
    n = len(figure)
    new_figure = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_figure[i][j] = figure[n - j - 1][i]
    return new_figure

if __name__ == '__main__':
    rotate90()