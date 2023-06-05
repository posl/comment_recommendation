def get_max_sum(n, m, cakes):
    max_sum = 0
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                sum = abs(cakes[i][0] + cakes[j][0] + cakes[k][0]) + abs(cakes[i][1] + cakes[j][1] + cakes[k][1]) + abs(cakes[i][2] + cakes[j][2] + cakes[k][2])
                if sum > max_sum:
                    max_sum = sum
    return max_sum

if __name__ == '__main__':
    get_max_sum()