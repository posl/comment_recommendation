def min_time(n, a, b):
    min_time = 1000000000000000000
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i] > b[j]:
                    if min_time > a[i]:
                        min_time = a[i]
                else:
                    if min_time > b[j]:
                        min_time = b[j]
            else:
                if min_time > a[i] + b[j]:
                    min_time = a[i] + b[j]
    return min_time

if __name__ == '__main__':
    min_time()