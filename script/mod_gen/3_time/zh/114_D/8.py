def count_divisor(n):
    if n == 1:
        return 1
    else:
        count = 2
        i = 2
        while i * i < n:
            if n % i == 0:
                count += 2
            i += 1
        if i * i == n:
            count += 1
        return count

if __name__ == '__main__':
    count_divisor()