def get_min_cost(h, w, c, a):
    min_cost = 1000000000000000000
    for i in range(h):
        for j in range(w):
            for p in range(h):
                for q in range(w):
                    if i == p and j == q:
                        continue
                    cost = a[i][j] + a[p][q] + c * (abs(i - p) + abs(j - q))
                    if cost < min_cost:
                        min_cost = cost
    return min_cost

if __name__ == '__main__':
    get_min_cost()