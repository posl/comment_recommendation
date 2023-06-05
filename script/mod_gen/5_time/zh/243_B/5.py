def count_same_position(n, a, b):
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count += 1
    return count

if __name__ == '__main__':
    count_same_position()