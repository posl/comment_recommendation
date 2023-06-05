def count_pairs(N, A):
    from collections import Counter
    counter = Counter(A)
    total = 0
    for v in counter.values():
        total += v * (v - 1) // 2
    return total

if __name__ == '__main__':
    count_pairs()