def count_odd_digits(num):
    count = 0
    for i in range(1, num + 1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

if __name__ == '__main__':
    count_odd_digits()