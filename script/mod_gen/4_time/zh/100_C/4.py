def get_max_operation_count(n, a):
    count = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            else:
                return count
        count += 1

if __name__ == '__main__':
    get_max_operation_count()