def count(n, m, a):
    count = [0] * m
    for i in range(n):
        count[a[i]] += 1
    return count

if __name__ == '__main__':
    count()