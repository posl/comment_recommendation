def count_div_by_2(num):
    count = 0
    while num % 2 == 0:
        count += 1
        num //= 2
    return count

if __name__ == '__main__':
    count_div_by_2()