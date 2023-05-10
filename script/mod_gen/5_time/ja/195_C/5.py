def comma_count(n):
    n_str = str(n)
    n_len = len(n_str)
    count = 0
    for i in range(1, n_len+1):
        if i % 3 == 0 and i != n_len:
            count += 1
    return count
n = int(input())
count = 0

if __name__ == '__main__':
    comma_count()