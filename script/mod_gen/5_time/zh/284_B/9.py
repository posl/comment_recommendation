def count_odd(n, a):
    count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            count += 1
    return count

if __name__ == '__main__':
    count_odd()