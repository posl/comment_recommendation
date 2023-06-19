def get_min_cost(n, c, l):
    min_cost = 0
    for i in range(n):
        min_cost += l[i][2]
    return min_cost

if __name__ == '__main__':
    get_min_cost()