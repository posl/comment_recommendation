def find_min_difference(N, W):
    min_diff = 1000000000
    for i in range(1, N):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == '__main__':
    find_min_difference()