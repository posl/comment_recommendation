def count_scream_times(a, b, k):
    if a >= b:
        return 0
    count = 0
    while a < b:
        a = a * k
        count += 1
    return count

if __name__ == '__main__':
    count_scream_times()