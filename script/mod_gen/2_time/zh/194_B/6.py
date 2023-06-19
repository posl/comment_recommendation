def find_min_time(n, a, b):
    min_time = 1000000
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[j]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    return min_time

if __name__ == '__main__':
    find_min_time()