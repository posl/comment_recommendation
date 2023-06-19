def min_times(n, k, a):
    min_times = 0
    for i in range(n):
        if i + k > n:
            break
        else:
            min_times += 1
            a[i:i+k] = [min(a[i:i+k])] * k
    return min_times

if __name__ == '__main__':
    min_times()