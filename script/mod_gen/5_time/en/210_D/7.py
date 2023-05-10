def find_min_cost(H, W, C, A):
    #print(H, W, C, A)
    min_cost = 1000000000000000000
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    if (i == k) and (j == l):
                        continue
                    cost = A[i][j] + A[k][l] + C * (abs(i - k) + abs(j - l))
                    if cost < min_cost:
                        min_cost = cost
    return min_cost

if __name__ == '__main__':
    find_min_cost()