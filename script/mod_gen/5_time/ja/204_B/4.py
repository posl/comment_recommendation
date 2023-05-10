def harvest(n, a):
    count = 0
    for i in range(n):
        if a[i] >= 10:
            count += a[i] - 10
    return count

if __name__ == '__main__':
    harvest()