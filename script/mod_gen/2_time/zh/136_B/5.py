def count_odd(n):
    if n < 10:
        return n
    else:
        count = 9
        for i in range(10, n + 1):
            if i % 10 % 2 == 1:
                count += 1
        return count

if __name__ == '__main__':
    count_odd()