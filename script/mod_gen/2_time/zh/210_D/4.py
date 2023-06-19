def min_cost(h, w, c, a):
    min_cost = 10**9 * h * w
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    cost = a[i][j] + a[k][l] + c * (abs(i-k) + abs(j-l))
                    if cost < min_cost:
                        min_cost = cost
    return min_cost

if __name__ == '__main__':
    min_cost()