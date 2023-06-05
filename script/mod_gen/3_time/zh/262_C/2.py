def count_pairs(a):
    n = len(a)
    pairs = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if min(a[i - 1], a[j - 1]) == i and max(a[i - 1], a[j - 1]) == j:
                pairs += 1
    return pairs

if __name__ == '__main__':
    count_pairs()