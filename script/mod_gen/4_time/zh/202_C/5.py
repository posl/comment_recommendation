def count_pairs(n, a, b, c):
    count = 0
    for i in range(n):
        for j in range(n):
            if a[i] == b[c[j] - 1]:
                count += 1
    return count

if __name__ == '__main__':
    count_pairs()