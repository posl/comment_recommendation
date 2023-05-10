def harvest(n, a):
    total = 0
    for i in range(n):
        if a[i] > 10:
            total += a[i] - 10
    return total

if __name__ == '__main__':
    harvest()