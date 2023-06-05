def get_min_diff(N, W):
    min_diff = 10000
    for i in range(1, N):
        sum1 = sum(W[:i])
        sum2 = sum(W[i:])
        if abs(sum1 - sum2) < min_diff:
            min_diff = abs(sum1 - sum2)
    return min_diff

if __name__ == '__main__':
    get_min_diff()