def find_max_times(n):
    result = 0
    for i in range(2, int(pow(n, 0.5))+1):
        if n % i == 0:
            while n % i == 0:
                n /= i
            result += 1
    if n != 1:
        result += 1
    return result

if __name__ == '__main__':
    find_max_times()