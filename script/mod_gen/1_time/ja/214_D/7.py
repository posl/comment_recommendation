def get_max_weight(n, edges):
    max_weight = 0
    for i in range(n):
        for j in range(i+1, n):
            max_weight = max(max_weight, edges[i][j])
    return max_weight

if __name__ == '__main__':
    get_max_weight()