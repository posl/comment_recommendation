def get_max_value(n, m, cakes):
    cakes.sort(key=lambda x: x[0] + x[1] + x[2])
    cakes.reverse()
    max_value = 0
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if i + j + k > m:
                    break
                value = abs(cakes[i][0]) + abs(cakes[j][1]) + abs(cakes[k][2])
                if value > max_value:
                    max_value = value
    return max_value
