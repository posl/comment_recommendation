def get_min_error(squares, n, c):
    min_error = 1000000000
    for i in range(c):
        for j in range(c):
            for k in range(c):
                if i != j and j != k and k != i:
                    error = 0
                    for l in range(n):
                        for m in range(n):
                            if (l + m) % 3 == 0:
                                error += squares[l][m][i]
                            elif (l + m) % 3 == 1:
                                error += squares[l][m][j]
                            elif (l + m) % 3 == 2:
                                error += squares[l][m][k]
                    min_error = min(min_error, error)
    return min_error

if __name__ == '__main__':
    get_min_error()