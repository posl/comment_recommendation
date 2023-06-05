def max_value(N, V, C):
    max_diff = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            diff = V[i] - C[j]
            if diff > max_diff:
                max_diff = diff
    return max_diff

if __name__ == '__main__':
    max_value()