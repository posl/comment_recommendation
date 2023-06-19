def get_max_sum(n, a):
    max_sum = 0
    count = 0
    for i in range(n):
        if a[i] < 0:
            count += 1
            a[i] = -a[i]
        max_sum += a[i]
    if count % 2 == 0:
        return max_sum
    else:
        return max_sum - 2 * min(a)

if __name__ == '__main__':
    get_max_sum()