def min_time(n,a,b):
    min_time = 0
    for i in range(n):
        if a[i] > b[i]:
            min_time += b[i]
        else:
            min_time += a[i]
    return min_time

if __name__ == '__main__':
    min_time()