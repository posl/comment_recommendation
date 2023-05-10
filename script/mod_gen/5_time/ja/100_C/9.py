def count_div2(num):
    count = 0
    while num % 2 == 0:
        count += 1
        num /= 2
    return count

if __name__ == '__main__':
    count_div2()