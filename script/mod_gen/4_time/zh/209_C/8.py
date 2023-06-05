def count_seq(n, c):
    c.sort()
    count = 1
    for i in range(n):
        count *= c[i] - i
        count %= (10 ** 9 + 7)
    return count

if __name__ == '__main__':
    count_seq()