def get_max_value(n, m, cakes):
    cakes.sort(key=lambda cake: abs(cake[0]) + abs(cake[1]) + abs(cake[2]), reverse=True)
    max_value = 0
    for i in range(m):
        max_value += abs(cakes[i][0]) + abs(cakes[i][1]) + abs(cakes[i][2])
    return max_value

if __name__ == '__main__':
    get_max_value()