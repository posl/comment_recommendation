def count_divisors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

if __name__ == '__main__':
    count_divisors()