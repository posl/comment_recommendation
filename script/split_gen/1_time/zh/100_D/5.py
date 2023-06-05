def get_max_value(cakes, m):
    cakes.sort(key=lambda x: abs(x[0]) + abs(x[1]) + abs(x[2]), reverse=True)
    values = []
    for i in range(1, 2**len(cakes)):
        cakes_selected = []
        for j in range(len(cakes)):
            if (i >> j) % 2 == 1:
                cakes_selected.append(cakes[j])
        if len(cakes_selected) == m:
            values.append(sum([abs(cake[0]) + abs(cake[1]) + abs(cake[2]) for cake in cakes_selected]))
    return max(values)
