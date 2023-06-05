def calc_sum(x, n):
    sum = 0
    for i in range(n):
        sum += (x - i) ** 2
    return sum

if __name__ == '__main__':
    calc_sum()