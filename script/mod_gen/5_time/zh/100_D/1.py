def get_max_value(n, m, cakes):
    cakes.sort(key=lambda x: x[0]-x[1]-x[2], reverse=True)
    result = 0
    for i in range(m):
        result += cakes[i][0]
    for i in range(m, n):
        result -= cakes[i][1]
    return result

if __name__ == '__main__':
    get_max_value()