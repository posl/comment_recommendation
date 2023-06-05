def get_sum(n, a, b):
    sum = 0
    for i in range(1, n+1):
        if i % a != 0 and i % b != 0:
            sum += i
    return sum

if __name__ == '__main__':
    get_sum()