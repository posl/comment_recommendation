def get_fizzbuzz_sum(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 15 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        else:
            pass
    return sum

if __name__ == '__main__':
    get_fizzbuzz_sum()